#include "preprocess.hpp"

static cv::Mat letterbox(const cv::Mat& src, int size) {
    int w = src.cols, h = src.rows;
    float scale = size / static_cast<float>(std::max(w, h));
    int new_w = static_cast<int>(w * scale);
    int new_h = static_cast<int>(h * scale);

    cv::Mat resized;
    cv::resize(src, resized, {new_w, new_h}, 0, 0, cv::INTER_LINEAR);

    int top    = (size - new_h) / 2;
    int bottom = size - new_h - top;
    int left   = (size - new_w) / 2;
    int right  = size - new_w - left;

    cv::Mat padded;
    cv::copyMakeBorder(resized, padded,
                       top, bottom, left, right,
                       cv::BORDER_CONSTANT, cv::Scalar(114, 114, 114));
    return padded;
}

cv::Mat preprocess(const cv::Mat& img, int dst, bool letterboxFlag) {
    cv::Mat rgb;
    if (img.channels() == 3)
        cv::cvtColor(img, rgb, cv::COLOR_BGR2RGB);
    else
        cv::cvtColor(img, rgb, cv::COLOR_GRAY2RGB);

    cv::Mat processed = letterboxFlag ? letterbox(rgb, dst)
                                      : cv::Mat();
    if (!letterboxFlag)
        cv::resize(rgb, processed, {dst, dst}, 0, 0, cv::INTER_LINEAR);

    processed.convertTo(processed, CV_32F, 1.0 / 255.0);
    return processed;          // NHWC, float32
}
