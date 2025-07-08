#pragma once
#include <opencv2/opencv.hpp>

/**
 * @brief YOLOv8'de kullanılmak üzere resmi yeniden boyutlandırır,
 *        opsiyonel letterbox uygular ve [0-1] float32 aralığına normalizer.
 *
 * @param img BGR veya GRAY OpenCV matrisi
 * @param dst_size Çıktı kenar uzunluğu (kare) – varsayılan 640
 * @param letterbox Kenar boşluğu ekleyerek oranı koru? (true)
 * @return cv::Mat  (CV_32FC3, NHWC formatında)
 */
cv::Mat preprocess(const cv::Mat& img,
                   int dst_size = 640,
                   bool letterbox = true);
