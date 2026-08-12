[app]
title = MikeyBot
package.name = mikeybot
package.domain = org.mikeybot

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,json,txt

version = 1.0

requirements = python3,kivy==2.2.1,requests,urllib3,certifi,idna,charset-normalizer

orientation = portrait
fullscreen = 0

android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.accept_sdk_license = True
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 0
