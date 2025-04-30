import tkinter as tk
from tkinter import messagebox
import phonenumbers
from phonenumbers import geocoder as phone_geocoder, carrier
import geocoder
from opencage.geocoder import OpenCageGeocode
import folium
import webbrowser
import datetime
import os

# Use your own API key here
OPENCAGE_API_KEY = "YOUR_OPENCAGE_API_KEY"

# Log file path
LOG_FILE = "location_logs.txt"

def log_result(input_data, result):
    with open(LOG_FILE, "a") as file:
        file.write(f"\n[{datetime.datetime.now()}] Input: {input_data} | Result: {result}\n")

def get_location_by_ip(ip):
    g = geocoder.ip(ip)
    if g.ok and g.latlng:
        return {
            "type": "ip",
            "city": g.city or "Unknown",
            "country": g.country or "Unknown",
            "coordinates": g.latlng
        }
    return None

def get_location_by_phone(number):
    try:
        parsed_number = phonenumbers.parse(number, None)
        location = phone_geocoder.description_for_number(parsed_number, "en")
        sim_carrier = carrier.name_for_number(parsed_number, "en")
        
        geocoder_oc = OpenCageGeocode(OPENCAGE_API_KEY)
        query = f"{location}"
        results = geocoder_oc.geocode(query)

        if results and 'geometry' in results[0]:
            coords = [results[0]['geometry']['lat'], results[0]['geometry']['lng']]
            return {
                "type": "phone",
                "city": location,
                "country": results[0]['components'].get('country', 'Unknown'),
                "carrier": sim_carrier,
                "coordinates": coords
            }
    except Exception as e:
        print("Phone location error:", e)
    return None

def show_map(coords, label):
    try:
        if coords:
            map_ = folium.Map(location=coords, zoom_start=10)
            folium.Marker(location=coords, popup=label, tooltip="Location").add_to(map_)
            map_file = "location_map.html"
            map_.save(map_file)
            webbrowser.open(map_file)
        else:
            raise ValueError("Coordinates are empty")
    except Exception as e:
        messagebox.showerror("Map Error", f"Failed to generate map: {e}")

def track():
    input_data = entry.get().strip()
    result = None

    if not input_data:
        messagebox.showwarning("Input Error", "Please enter an IP address or phone number.")
        return

    # Decide based on input pattern
    if input_data.replace(".", "").isdigit():  # Likely IP address
        result = get_location_by_ip(input_data)
    else:  # Treat as phone number
        result = get_location_by_phone(input_data)

    if result and result.get("coordinates"):
        details = f"Type: {result['type'].capitalize()}\nCity: {result['city']}\nCountry: {result['country']}\nCoordinates: {result['coordinates']}"
        if result['type'] == "phone":
            details += f"\nCarrier: {result.get('carrier', 'N/A')}"
        messagebox.showinfo("Location Info", details)
        log_result(input_data, details)
        show_map(result['coordinates'], result['city'])
    else:
        messagebox.showerror("Tracking Failed", "Could not retrieve location. Check your input or network connection.")
        log_result(input_data, "Tracking failed.")

# GUI setup
root = tk.Tk()
root.title("IP / Phone Location Tracker")
root.geometry("400x200")
root.config(bg="#f0f0f0")

title = tk.Label(root, text="Location Tracker", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14), width=30)
entry.pack(pady=10)

track_button = tk.Button(root, text="Track", font=("Helvetica", 12), command=track)
track_button.pack(pady=5)

footer = tk.Label(root, text="Enter IP Address or Phone Number", font=("Helvetica", 10), bg="#f0f0f0", fg="gray")
footer.pack(side="bottom", pady=5)

root.mainloop()
