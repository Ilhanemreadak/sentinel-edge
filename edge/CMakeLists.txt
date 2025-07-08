# Library: preprocess
add_library(preprocess STATIC
    src/preprocess.cpp
)
target_include_directories(preprocess PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(preprocess PUBLIC opencv_core opencv_imgproc)

# Executable: rtsp_reader
add_executable(rtsp_reader
    src/rtsp_reader.cpp
)
target_include_directories(rtsp_reader PRIVATE ${CMAKE_CURRENT_SOURCE_DIR}/include)
target_link_libraries(rtsp_reader PRIVATE
    preprocess
    opencv_core opencv_videoio opencv_imgcodecs opencv_highgui
)

# ------------ (Opsiyonel) GoogleTest birimleri -------------
option(ENABLE_TESTS "Build unit tests" OFF)
if(ENABLE_TESTS)
    find_package(GTest REQUIRED)
    enable_testing()
    add_executable(test_preprocess tests/test_preprocess.cpp)
    target_link_libraries(test_preprocess PRIVATE preprocess GTest::gtest_main)
    add_test(NAME preprocess_test COMMAND test_preprocess)
endif()
