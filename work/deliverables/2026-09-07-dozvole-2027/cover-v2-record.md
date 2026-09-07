# Cover revision — remove rod

Owner requested removal of the rod because it incorrectly disappeared into the reel. Built-in imagegen precise-object-edit was used on cover.png; original preserved, revised source saved as cover-v2.png. No CLI fallback used.

Generated source: /root/.codex/generated_images/01a07ad4-cd5c-7a50-956b-d366ced9672f/exec-0f3e1d2e-8a15-48f2-8588-27290715e766.png

Visual inspection: entire rod and cork grip removed, leaving cream paper. Reel retains its mounting foot, stem, spool, bail and crank. Booklet and orange float remain in position, with the same cream/pine gouache style. No new text, logos or objects.

New alt: Ilustracija zelene ribolovačke knjižice, mašinice i narandžastog plovka.
Public caption remains Sve Za Pecanje; credit field empty.

## Exact edit prompt

Use case: precise-object-edit. Input image 1 is the edit target: the current gouache cover illustration. Remove ONLY the fishing rod: erase the entire diagonal rod blank, both cork grips, and black cylindrical reel-seat parts along the right side, including any rod remnants behind the reel's mounting foot. Fill those areas with the same warm cream paper texture and appropriate subtle shadows for the remaining objects. Keep the spinning reel intact as a detached standalone reel, including its metal mounting stem and foot, spool, bail wire, body and crank handle. Preserve the green booklet with fish silhouette, orange float, their positions and scale, the reel's position and scale, all other object details, gouache brushwork, cream-and-pine palette, paper grain, original lighting, landscape framing and image dimensions. No new objects, text, logos, borders or watermark. The final scene contains only a booklet, a detached reel and a float on cream paper; absolutely no fishing rod or cork grip.

## Deployment verification

CMS post 2 now references new media 3. Original media 2 and original cover.png retained for rollback; historical publication evidence remains unchanged. Article body and firstPublishedAt (2026-09-07T21:40:23.511Z) verified unchanged; post remains published.

Public article and blog index checked at 1440 and 390 px: HTTP 200, revised image loaded, revised descriptive alt, no horizontal overflow or JavaScript page errors. Screenshots saved as cover-v2-{article,index}-{1440,390}.png. Social-preview metadata uses the new media URL, which returns 200. Article canonical unchanged. Mobile screenshot visually inspected; all three remaining objects fit and no rod remains.

Brand validation and whitespace checks passed. No application code change, deployment or Git commit/push. Revised public image: https://tipsforwins.fsn1.your-objectstorage.com/media/d2e49fa8-553a-4203-9c2d-305c50e8cb7b.webp
