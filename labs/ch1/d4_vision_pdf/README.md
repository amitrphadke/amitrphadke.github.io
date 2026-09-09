# Lab 1.4 — Image and PDF content blocks

**Pairs with:** Image support · PDF support · Citations

## Task
1. `image_block_from_file(path)` → `{"type":"image","source":{"type":"base64","media_type":..., "data":...}}` (detect media type from the extension).
2. `image_block_from_url(url)` → `{"type":"image","source":{"type":"url","url":url}}`.
3. `pdf_block_from_file(path)` → `{"type":"document","source":{"type":"base64","media_type":"application/pdf","data":...}}`; add `"citations":{"enabled":True}`.
4. `describe(blocks, question)` sends the blocks plus a text block and returns the reply text.

The folder has `sample.png` (a 2-colour test image) and `sample.pdf` (one page saying "CCDV-F LAB PDF 2026").

## Exam angles
- Content is a **list of blocks**; images/documents go in the *user* message.
- Limits to write down: image ≤ 5 MB / 8000 px per image, up to 20 images (API) per request; PDFs up to 32 MB and 100 pages; PDFs count as text + one image per page.
