# 📍 Location Tracker

A Python-based desktop application that allows users to track IP addresses and phone numbers to identify their approximate geographical location. The project features a Tkinter-based GUI, geolocation data extraction, and map visualization using Folium.

## 🚀 Features

- 🌐 Track IP addresses with region, country, city, and coordinates.
- 📞 Track phone number location using country code and carrier data.
- 🗺️ Visualize locations on an interactive Folium map.
- 💾 Log and save tracking results.
- ✅ Easy-to-use graphical interface built with Tkinter.

## 🛠️ Tech Stack

- Python 3.x
- [Tkinter](https://docs.python.org/3/library/tkinter.html) - GUI toolkit
- [requests](https://pypi.org/project/requests/) - API calls
- [folium](https://pypi.org/project/folium/) - Map visualization
- [phonenumbers](https://pypi.org/project/phonenumbers/) - Phone number geolocation
- [OpenCage Geocoder](https://opencagedata.com/) - Reverse geocoding API

## 📂 Project Structure

```
location_tracker/
├── location_tracker.py
├── README.md
├── requirements.txt
└── venv/ (optional)
```

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/location_tracker.git
   cd location_tracker
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python location_tracker.py
   ```

## 📌 API Key Required

This app uses the OpenCage Geocoding API.

1. Sign up at [https://opencagedata.com/](https://opencagedata.com/)
2. Get your free API key.
3. Add it in the script file where prompted:
   ```python
   OPENCAGE_API_KEY = "your_api_key_here"
   ```

## 🧪 Usage

- Enter an IP address or phone number in the app window.
- Click "Track".
- View the results and open the map.
- Results include city, region, country, carrier (for phone), and coordinates.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by Akanksha
