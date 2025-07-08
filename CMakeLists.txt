cmake_minimum_required(VERSION 3.25)
project(sentinel_edge LANGUAGES CXX)

# Varsayılan C++17
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# OpenCV bul (pkg-config yerine)
find_package(OpenCV REQUIRED core imgproc imgcodecs videoio highgui)

# Alt dizine geç
add_subdirectory(edge)
