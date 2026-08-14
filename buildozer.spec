[app]

# -----------------------------------------------------------------
# APP INFORMATION
# -----------------------------------------------------------------

title = Mikey Bot
package.name = mikeybot
package.domain = org.mikeybot

version = 1.0.0

# -----------------------------------------------------------------
# SOURCE
# -----------------------------------------------------------------

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt
source.exclude_dirs = tests,bin,venv,.venv,.buildozer,.git,.github
source.exclude_patterns = *.pyc,*.pyo,__pycache__/*,license,.gitignore

# -----------------------------------------------------------------
# PYTHON / KIVY REQUIREMENTS
# -----------------------------------------------------------------

requirements = python3==3.10.11,hostpython3==3.10.11,kivy==2.3.0

# -----------------------------------------------------------------
# DISPLAY
# -----------------------------------------------------------------

orientation = portrait
fullscreen = 0

# -----------------------------------------------------------------
# ANDROID
# -----------------------------------------------------------------

android.permissions = INTERNET,ACCESS_NETWORK_STATE

android.api = 33
android.minapi = 21
android.ndk = 25b

android.accept_sdk_license = True
android.enable_androidx = True

android.archs = arm64-v8a

# -----------------------------------------------------------------
# PYTHON-FOR-ANDROID
# -----------------------------------------------------------------

p4a.fork = kivy
p4a.branch = master

# -----------------------------------------------------------------
# BUILD
# -----------------------------------------------------------------

[buildozer]

log_level = 2
warn_on_root = 0
