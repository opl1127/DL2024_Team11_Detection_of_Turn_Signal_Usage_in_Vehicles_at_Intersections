# Deep learning 期末專案
路口方向燈偵測

#背景
隨著城市化的進程加快，交通問題日益突出。
交通信號燈在維持交通秩序和提高交通效率方面起著重要作用。
特別是路口的方向燈（左轉燈、直行燈、右轉燈）對於確保行車安全和減少交通事故至關重要。
因此，開發一個能夠自動識別路口方向燈狀態的系統，有助於提升交通管理水平。

目標
設計並實現一個基於計算機視覺的路口方向燈偵測系統，能夠自動識別路口車輛狀態(左轉、直行、右轉)，以及路口車輛方向燈狀態(正確施打方向燈，為正確施打方向燈)。

主要內容
1.數據收集與標註
	•	收集包含不同天氣條件和時間段的路口方向燈圖片和視頻數據。
	•	標註數據集，標記每張圖片中的方向燈狀態(左轉燈、直行燈、右轉燈)。
2.影像處理與特徵提取
    •       將影片分幀
	•	使用labelImg，提取方向燈區域。
	•	使用深度學習模型(Yolo v8)進行方向燈狀態的識別。
3.模型訓練與評估
	•	使用標註好的數據集訓練模型，調整參數以提高準確性。
	•	在測試集上評估模型性能，確保其在實際應用中的可靠性。



# 使用工具

