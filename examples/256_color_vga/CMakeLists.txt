cmake_minimum_required(VERSION 2.8.9)
# IncludeOS install location
if (NOT DEFINED ENV{INCLUDEOS_PREFIX})
  set(ENV{INCLUDEOS_PREFIX} /usr/local)
endif()
include($ENV{INCLUDEOS_PREFIX}/includeos/pre.service.cmake)
project (256_color_vga)

# Human-readable name of your service
set(SERVICE_NAME "256 Color VGA Example Service")

# Name of your service binary
set(BINARY       "vga_gfx")

# Source files to be linked with OS library parts to form bootable image
set(SOURCES
  service.cpp
  )

# include service build script
include($ENV{INCLUDEOS_PREFIX}/includeos/post.service.cmake)
