#include <opencv2/opencv.hpp>
#include <iostream>
#include <chrono>
#include <filesystem>
#include <locale>

/*
 * Edge RTSP reader prototype
 *  - Bağlantıyı açar, kareleri stdout'a yazar.
 *  - Reads an RTSP URL, prints frame info, optionally saves first N frames.
 */

int main(int argc, char** argv) {
    std::setlocale(LC_ALL, "C");      // Konsol Türkçe kodlamaya takılmasın // force English locale

    if (argc < 2) {
        std::cerr << "Usage: " << argv[0]
                  << " <rtsp_url|video_file> [--save n_frames]\n";
        return 1;
    }

    std::string rtsp_url = argv[1];
    int save_n = 0;
    if (argc == 4 && std::string(argv[2]) == "--save") {
        save_n = std::stoi(argv[3]);
        std::filesystem::create_directories("tmp");
    }

    // FFMPEG backend is most reliable for RTSP on Windows/Linux
    cv::VideoCapture cap(rtsp_url, cv::CAP_FFMPEG);
    if (!cap.isOpened()) {
        std::cerr << "ERROR: Unable to open stream ➜ " << rtsp_url << '\n';
        return 2;
    }
    std::cout << "Connected: " << rtsp_url << std::endl;

    cv::Mat frame;
    int idx = 0;
    while (cap.read(frame)) {
        auto ts = std::chrono::system_clock::now();
        auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(
                      ts.time_since_epoch())
                      .count();
        std::cout << "[#" << idx << "] "
                  << frame.cols << "x" << frame.rows
                  << " @" << ms << " ms" << std::endl;

        if (save_n > 0 && idx < save_n) {
            std::string fn = "tmp/frame_" + std::to_string(idx) + ".jpg";
            cv::imwrite(fn, frame);
        }
        ++idx;
        // Small sleep to avoid 100% CPU (GUI-less). FPS yüksekse yoruma alabilirsiniz.
        cv::waitKey(1);
    }

    std::cout << "Stream ended or connection lost." << std::endl;
    return 0;
}