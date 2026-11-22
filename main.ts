// Entry point for the 22 November 2026 news-image entry.
//
// The picture itself is already finished and stored in this repository
// as entry.png, so all this program has to do is hand an exact copy of
// it to the grader. It reads the file sitting next to this script and
// writes those same bytes to entry.png inside the output folder the
// environment points at (or /output when nothing is set). Because the
// file is only copied, never redrawn, two runs always produce identical
// bytes.
//
// After copying, the program re-reads both files and compares their
// SHA-256 digests, so a truncated or corrupted write is reported as a
// failure instead of silently handing the grader a broken image.
import { copyFileSync, existsSync, mkdirSync, readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

function sha256Of(path: string): string {
  return createHash("sha256").update(readFileSync(path)).digest("hex");
}

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

if (!existsSync(source)) {
  console.error(`error: source image not found: ${source}`);
  process.exit(1);
}

mkdirSync(outDir, { recursive: true });
const destination = join(outDir, "entry.png");
copyFileSync(source, destination);

const sourceHash = sha256Of(source);
const writtenHash = sha256Of(destination);
if (sourceHash !== writtenHash) {
  console.error(
    `error: copied entry.png failed integrity check: ` +
      `source sha256=${sourceHash}, written sha256=${writtenHash}`,
  );
  process.exit(1);
}
console.log(`wrote entry.png sha256=${writtenHash}`);
