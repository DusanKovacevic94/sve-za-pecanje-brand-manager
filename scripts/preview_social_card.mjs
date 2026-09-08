/** Task 080 design proof only. Production CMS rendering is task 081. */
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { createRequire } from 'node:module';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const app = path.resolve(process.env.SZP_APP_REPO || path.join(root, '../sve-za-pecanje'));
const require = createRequire(path.join(app, 'frontend/package.json'));
const { chromium } = require('@playwright/test');
const sharp = createRequire(path.join(app, 'cms/package.json'))('sharp');
const output = path.join(root, 'work/deliverables/2026-09-08-social-blog-cards');
const template = await readFile(path.join(root, 'assets/social/blog-card.svg'), 'utf8');
const layout = JSON.parse(await readFile(path.join(root, 'assets/social/blog-card-layout.json'), 'utf8'));
const font = await readFile(path.join(root, 'assets/fonts/Manrope-variable.ttf'));
const logo = await readFile(path.join(root, 'assets/logos/logo-inverse.svg'));
assert.equal(createHash('sha256').update(font).digest('hex'), 'd0639be45d0af36e798172419d7bd173c4bd4f29e2b76cbb69db1d11bf8b0a40');
assert.equal(createHash('sha256').update(logo).digest('hex'), '16cf2a6afa6c84482bfc099e367a804d623a8a02e61097b8a77080cd8c13d221');
assert.ok(template.includes(`data:image/svg+xml;base64,${logo.toString('base64')}`), 'Embedded logo must match the protected inverse export byte for byte');
const escapeXML = (value) => value.replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&apos;' })[c]);
const normalize = (value, field) => {
  if (typeof value !== 'string' || value.length > 1000 || /[^\u0020-\u007e\u00a0-\u024f\u2013\u2014\u2018-\u201f\u2026\n\r\t]/u.test(value.normalize('NFC'))) throw Error(`${field}: unsupported text`);
  const text = value.normalize('NFC').replace(/\s+/gu, ' ').trim();
  if (!text || [...text].length > layout[field].maxCharacters) throw Error(`${field}: shorten copy`);
  return text;
};
await mkdir(output, { recursive: true });
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
await page.route('**/*', route => route.abort());
const reports = [];
try {
  await page.evaluate(async (data) => {
    const font = new FontFace('Manrope', `url(data:font/ttf;base64,${data})`, { weight: '200 800' });
    document.fonts.add(await font.load());
  }, font.toString('base64'));

  async function compose(input, direction = 'editorial') {
    const title = normalize(input.title, 'title');
    const description = normalize(input.description, 'description');
    const lines = await page.evaluate(({ title, description, layout }) => {
      const canvas = document.createElement('canvas');
      const context = canvas.getContext('2d');
      const wrap = (text, spec, field) => {
        context.font = `${spec.fontWeight} ${spec.fontSize}px Manrope`;
        const lines = [];
        for (const word of text.split(' ')) {
          if (context.measureText(word).width > spec.maxWidth) throw Error(`${field}: word exceeds width`);
          const last = lines.at(-1);
          if (last && context.measureText(`${last} ${word}`).width <= spec.maxWidth) lines[lines.length - 1] += ` ${word}`;
          else lines.push(word);
        }
        if (lines.length > spec.maxLines) throw Error(`${field}: shorten copy to fit ${spec.maxLines} lines`);
        return lines;
      };
      return { title: wrap(title, layout.title, 'title'), description: wrap(description, layout.description, 'description') };
    }, { title, description, layout });
    const tags = (field) => lines[field].map((line, i) => {
      const spec = layout[field];
      const first = field === 'title' ? spec.centerBaseline - (lines[field].length - 1) * spec.lineHeight / 2 : spec.firstBaseline;
      return `<text x="540" y="${first + i * spec.lineHeight}">${escapeXML(line)}</text>`;
    }).join('\n');
    const values = { TITLE: escapeXML(title), DESCRIPTION: escapeXML(description), FONT: font.toString('base64'), LOGO: logo.toString('base64'), TITLE_LINES: tags('title'), DESCRIPTION_LINES: tags('description') };
    let svg = template.replace(/\{\{([A-Z_]+)\}\}/g, (_, key) => values[key]);
    if (direction === 'framed') {
      svg = svg.replace('<rect width="1080" height="1350" fill="#173F37"/>', '<rect width="1080" height="1350" fill="#173F37"/><rect x="48" y="298" width="984" height="720" rx="16" fill="#F7F6F1"/>');
      svg = svg.replaceAll('<g fill="#F7F6F1" text-anchor="middle"', '<g fill="#173F37" text-anchor="middle"');
    }
    return { svg, lines };
  }

  const examples = [
    { name: 'editorial', title: 'Kako izabrati prvu mašinicu?', description: 'Veličina, prenos i kočnica: šta je važno pri izboru opreme za tvoj način ribolova.' },
    { name: 'framed', title: 'Kako izabrati prvu mašinicu?', description: 'Veličina, prenos i kočnica: šta je važno pri izboru opreme za tvoj način ribolova.' },
    { name: 'short', title: 'Vidimo se na vodi.', description: 'Novosti iz naše ribolovačke zajednice.' },
    { name: 'long', title: 'Štapovi, mašinice i varalice: priprema za izlazak na vodu', description: 'Proveri spojeve, očisti opremu i izdvoji ono što nosiš. Kratak pregled pripreme, od štapa i mašinice do sitnog pribora koji se lako zaboravi.' },
    { name: 'diacritics', title: 'Čuvar reke: đaci čiste obalu', description: 'Č ć ž š đ — Đorđe kaže: „Sačuvajmo reku.” O ljudima, druženju i događajima koji povezuju ribolovce.' },
    { name: 'punctuation', title: 'Štap < 2 m & mašinica?', description: 'Doslovan tekst, ne HTML: „izbor” & „održavanje”. Detalji za čitaoce, bez skrivenog sadržaja.' },
    { name: 'limits', title: 'Izbor niti i sitni pribor: '.padEnd(100, 'i'), description: 'Sitni pribor i niti za ribolov. '.repeat(6).slice(0, 180).padEnd(180, '.') },
  ];
  // Use short words at the character boundary; width is a separate hard constraint.
  examples.at(-1).title = ('Izbor niti i sitni pribor. '.repeat(5)).slice(0, 99) + '.';
  for (const example of examples) {
    const result = await compose(example, example.name);
    await page.setContent(`<html><head><style>html,body{margin:0}svg{display:block}</style></head><body>${result.svg}</body></html>`);
    await page.evaluate(async () => { await document.fonts.load('800 76px Manrope'); await document.fonts.load('400 34px Manrope'); await document.fonts.load('500 30px Manrope'); await document.fonts.ready; });
    const geometry = await page.locator('svg > g > text').evaluateAll(elements => elements.map(el => {
      const box = el.getBBox();
      return { text: el.textContent, x: box.x, y: box.y, width: box.width, height: box.height };
    }));
    for (const box of geometry) {
      assert.ok(box.x >= layout.safeMargin && box.x + box.width <= 1080 - layout.safeMargin, JSON.stringify(box));
      assert.ok(box.y >= 298 && box.y + box.height < 1000, JSON.stringify(box));
    }
    await writeFile(path.join(output, `${example.name}.svg`), result.svg);
    const jpeg = await page.locator('svg').screenshot({ type: 'jpeg', quality: layout.jpeg.quality });
    assert.ok(jpeg.length < layout.jpeg.maxBytes);
    await writeFile(path.join(output, `${example.name}.jpg`), jpeg);
    const meta = await sharp(jpeg).metadata();
    assert.equal(meta.width, layout.width);
    assert.equal(meta.height, layout.height);
    // Phone proof is a real browser rendering of the same SVG, not a separate layout.
    await page.addStyleTag({ content: 'svg{width:390px;height:487.5px}' });
    await page.locator('svg').screenshot({ path: path.join(output, `${example.name}-phone.png`) });
    reports.push({ name: example.name, titleCharacters: [...example.title].length, descriptionCharacters: [...example.description].length, lines: result.lines, jpegBytes: jpeg.length, geometry });
  }
  const valid = examples[0];
  await assert.rejects(compose({ ...valid, title: 'W'.repeat(40) }), /word exceeds width/);
  await assert.rejects(compose({ ...valid, title: 'WIDE '.repeat(20).trim() }), /shorten copy/);
  await assert.rejects(compose({ ...valid, title: 'a'.repeat(101) }), /shorten copy/);
  await assert.rejects(compose({ ...valid, description: 'a'.repeat(181) }), /shorten copy/);
  await assert.rejects(compose({ ...valid, title: 'hidden\u202e' }), /unsupported text/);
  await assert.rejects(compose({ ...valid, title: '' }), /shorten copy/);
  await assert.rejects(compose({ ...valid, title: 'Fish 🎣' }), /unsupported text/);
  const escaped = await compose({ ...valid, title: '<script> & "č"' });
  assert.ok(escaped.svg.includes('&lt;script&gt; &amp; &quot;č&quot;'));
  assert.ok(!escaped.svg.includes('<script>'));
  assert.equal((await compose({ ...valid, title: 'c\u030c' })).svg, (await compose({ ...valid, title: 'č' })).svg);
  const repeat = await compose(valid);
  assert.equal(repeat.svg, await readFile(path.join(output, 'editorial.svg'), 'utf8'));
  await writeFile(path.join(output, 'layout-checks.json'), JSON.stringify({ layoutVersion: layout.version, checks: 'bounds, JPEG dimensions/size, max length, width overflow, escaping, invisible controls, determinism, protected logo/font hashes', examples: reports }, null, 2) + '\n');
  console.log(`Passed: ${examples.length} full-size/phone proofs and negative layout checks. Output: ${output}`);
} finally {
  await browser.close();
}
