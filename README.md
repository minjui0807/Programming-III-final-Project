# Programming III Final Project

## 個人支出管理與分析系統

本專案為 Programming III 課程期末專題，實作一套 **個人支出管理與分析系統**。系統採用 **FastAPI** 作為後端框架，前端使用 **HTML + JavaScript**，並以 **SQLite** 作為資料庫，提供支出紀錄、分類管理與消費分析等功能。

---

## 使用技術

* Python 3.10+
* FastAPI
* SQLite
* HTML / JavaScript

---

## 專案目錄結構

```
Programming-III-final-Project-main/
│
├─ app/                     # 後端主程式
│  ├─ main.py               # FastAPI 進入點
│  ├─ config.py             # 系統設定
│  ├─ database.py           # 資料庫連線與初始化
│  ├─ deps.py               # 相依注入
│  └─ services/             # 商業邏輯層
│     ├─ expense_service.py # 支出 CRUD 邏輯
│     └─ analysis_service.py# 消費分析邏輯
│
├─ frontend/                # 前端頁面
│  ├─ index.html            # 首頁
│  ├─ recordpage.html       # 支出紀錄頁
│  ├─ category.html         # 分類管理頁
│  ├─ report.html           # 分析報表頁
│  └─ settings.html         # 系統設定頁
│
├─ expenses.db              # SQLite 資料庫
├─ requirements.txt         # Python 套件需求
└─ README.md                # 專案說明文件
```

---

## 系統功能說明

### 後端模組

#### `main.py`

* FastAPI 應用程式入口
* 負責 API 路由註冊與伺服器啟動

#### `database.py`

* 建立 SQLite 資料庫連線
* 初始化資料表
* 提供共用資料庫存取方法

#### `expense_service.py`

* 支出資料的 CRUD 功能：

  * 新增支出
  * 查詢支出
  * 修改支出
  * 刪除支出

#### `analysis_service.py`

* 消費資料分析功能
* 提供各分類支出統計與分析結果

---

### 前端頁面

* **index.html**：系統首頁與導覽
* **recordpage.html**：支出新增與查詢
* **category.html**：消費分類管理
* **report.html**：消費分析報表顯示
* **settings.html**：系統設定頁面

前端透過 JavaScript 呼叫後端 API 與資料庫進行互動。

---

## 系統安裝與執行方式

### 環境需求

* Python 3.10 以上
* pip 套件管理工具

### 安裝套件

```bash
pip install -r requirements.txt
```

### 啟動後端伺服器

```bash
uvicorn app.main:app --reload
```

啟動後可使用以下連結：

* Swagger API 文件：[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc API 文件：[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 執行測試方法

### 方法一：Swagger UI 測試（建議）

1. 啟動後端伺服器
2. 開啟瀏覽器進入：

   ```
   http://127.0.0.1:8000/docs
   ```
3. 選擇欲測試的 API
4. 點擊 **Try it out**
5. 輸入測試資料並執行
6. 確認回傳結果是否正確

---

### 方法二：前端操作測試

1. 啟動後端 API
2. 直接開啟 `frontend/index.html`
3. 透過網頁進行操作：

   * 新增支出紀錄
   * 查詢支出資料
   * 查看消費分析報表
4. 確認畫面顯示資料是否正確

---

### 方法三：cURL 指令測試（進階）

```bash
curl -X GET http://127.0.0.1:8000/expenses
```

---

## 測試檢查重點

* 支出資料是否能正確新增、修改與刪除
* 各分類統計金額是否正確
* 前後端資料是否同步
* 系統在資料為空時是否能正常運作

---

## 結論

本專案採用前後端分離架構，透過 FastAPI 建立 RESTful API，並搭配 SQLite 作為輕量化資料庫，使系統具備良好的可讀性、可維護性與測試性，適合作為 Programming III 課程之期末專題專案。
