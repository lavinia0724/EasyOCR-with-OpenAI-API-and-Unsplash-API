# LAVI's EasyOCR with OpenAI API and Unsplash API Side Project
利用 [Unsplash API](https://unsplash.com/) download dataset、透過 [OpenAI API model image to image](https://platform.openai.com/docs/api-reference/images)、使用 easyOCR text detection

## Information 
### Details

#### 1. 利用 Unsplash API 下載 Unsplash dataset 中指定類型的圖片
- 先於 Unsplash 註冊帳號成為 Developer 後進入[Application 頁面](https://unsplash.com/oauth/applications)創建自己的 App 後獲得 Access Key
- 我撰寫了 `UnsplashDownloadImage.py`，給予 keyword 及張數來下載圖片

#### 2-1. 透過 OpenAI API 將從 Unsplash 下載的圖生成 variation 變化圖
- 我撰寫了 `ImageToImageWithOpenAI.py` 將方才從 Unsplash API 下載的圖藉由 OpenAI API model 訓練並生成相似變化圖
	- 因為 OpenAI API 只吃 `.png`，而從 Unsplash API 下載的圖片是 `.jpg`，所以要轉檔

#### 2-2. 透過 OpenAI API prompt 生成圖片
- 先利用命令生成圖片模型 `openai api image.create -p “license plate from an image with many cars”`
	- 目前嘗試，如果沒有這行指令執行 `create.py` 都會噴錯誤
- 參考 [Generate Images With DALL·E 2 and the OpenAI API](https://realpython.com/generate-images-with-dalle-openai-api/) 文章後撰寫 `create.py` ，執行後會產出含生成圖片的 `.json` 檔並顯示圖片 URL
	- `create_v1.py` 及 `create_v2.py` 皆為直接輸出圖片 URL，而 `create_v3.py` 會將圖片自動下載於 `responses` 資料夾中	
- 利用 `convert.py` 將上一步生成的 `.json` 檔轉換為 `.png` 圖片
	
#### 3. 使用 easyOCR 進行圖片中可辨識之文字提取
- 參考 [EasyOCR tutorial](https://lablab.ai/t/easyocr-and-gpt-extraction-summarization) 文章後修改了 `easyOCR.py`
- 可將方才利用 OpenAI 生成之圖片 `generated_image.png` 中的文字進行偵測辨識讀取

## Reference
- [chatGPT](https://chat.openai.com/)
- [Unsplash API Documentation](https://unsplash.com/documentation#get-a-photo)
- [EasyOCR tutorial: Text extraction and summarization with EasyOCR and GPT-3!](https://lablab.ai/t/easyocr-and-gpt-extraction-summarization)
- [Generate Images With DALL·E 2 and the OpenAI API](https://realpython.com/generate-images-with-dalle-openai-api/)
- [OpenAI create images API documentation](https://platform.openai.com/docs/api-reference/images)



