import subprocess
import sys

# Configuration
BUILD_DIR          = "build"
PROJECT_DIR        = "src"
PLATFORM_TOOLSET   = "v143"
F4SE_REVISION      = "v0.7.2"
DIST_DIR           = "dist"

# Run build tools
p = subprocess.run([
    sys.executable,
    "tools/build-tools/build_plugin.py",
    "--build-dir", BUILD_DIR,
    "--project-dir", PROJECT_DIR,
    "--dist-dir", DIST_DIR,
    "--f4se-revision", F4SE_REVISION,
    "--platform-toolset", PLATFORM_TOOLSET,
])

raise SystemExit(p.returncode)
