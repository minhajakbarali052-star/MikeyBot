[app]

# (str) Title of your application
title = Mikey Bot

# (str) Package name
package.name = mikeybot

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mikeybot

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files / directories to exclude
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv, .buildozer, .git, .github
source.exclude_patterns = license, .gitignore, .github/*, */test/*, */tests/*

# (string) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy

# (str) Python-for-Android Branch (CRITICAL FIX: Fixes Lib/test compilation crash)
p4a.branch = develop

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET,NETWORK_STATE

# (int) Target Android API
android.api = 33

# (int) Minimum API support
android.minapi = 21

# (int) Android NDK API
android.ndk_api = 21

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (list) Pattern to blacklist / ignore during compilation
android.blacklist_patterns = sqlite3/*,lib-dynload/test/*,lib-dynload/json/tests/*,*/test/*,*/tests/*,*/Lib/test/*

# (bool) Enable AndroidX support
android.enable_androidx = True

# (list) Target architecture
android.archs = arm64-v8a

[buildozer]

# (int) Log level
log_level = 2

# (int) Display warning if run as root
warn_on_root = 0
