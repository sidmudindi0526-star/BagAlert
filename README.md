# BagAlert

Never forget your reusable bags again. BagAlert is a location-aware PWA that reminds you to grab your bags when you're heading to the grocery store.

## How It Works

1. **Add your home** — search by address or use GPS
2. **Add your stores** — search for nearby grocery stores by name or address
3. **Go about your day** — BagAlert tracks your location in the background
4. **Get reminded** — when you leave home or approach a store, you get an alert to grab your bags

## Features

- **Address search with autocomplete** — powered by OpenStreetMap/Nominatim (free, no API key needed)
- **Interactive map** — see your home, stores, and current location on an OpenStreetMap-based map
- **Geofence alerts** — configurable radius around each store and your home
- **Smart home alerts** — only triggers when you're likely driving (speed-based detection), not just walking around the neighborhood
- **Multi-sample GPS** — takes multiple readings and picks the most accurate one for precise home placement
- **Proximity-sorted search results** — nearby stores appear first, with distance shown in miles/feet
- **Notification history** — view past alerts with timestamps
- **Adjustable cooldowns** — control how often repeat alerts fire (5–120 minutes)
- **PWA / installable** — add to your phone's home screen and use it like a native app
- **Offline-capable** — service worker caches the app for offline use
- **Fully private** — all data stored locally on your device (browser localStorage), no accounts, no server

## Tech Stack

- **Flutter Web** (Dart)
- **flutter_map** + OpenStreetMap tiles (free map, no API key)
- **Nominatim API** for place search and geocoding
- **Geolocator** for GPS tracking and position streams
- **SharedPreferences** for local persistence (localStorage on web)
- **Provider** for state management

## Running Locally

```bash
# Run in Chrome (dev mode)
flutter run -d chrome

# Build production PWA
flutter build web --release

# Serve the build locally
python -m http.server 8080 --directory build/web
```

### Serving to phones on your local network

Phones require HTTPS for geolocation. A self-signed cert + HTTPS server script is included:

```bash
python serve_https.py
# Then open https://<your-local-ip>:4443 on your phone
```

## Project Structure

```
lib/
  main.dart                  # App entry point
  app.dart                   # MaterialApp + routing
  models/
    store_model.dart         # Grocery store data model
    home_location.dart       # Home location with address + geofence radius
    app_settings.dart        # User preferences (tracking, cooldown, etc.)
    notification_entry.dart  # Alert history entry
  providers/
    app_state.dart           # Central state (ChangeNotifier + Provider)
  screens/
    home_screen.dart         # Dashboard / main screen
    map_screen.dart          # Interactive map view
    stores_screen.dart       # Store list
    store_form_screen.dart   # Add/edit store with address search
    settings_screen.dart     # Home location, tracking, cooldown settings
    notifications_screen.dart # Alert history
  services/
    geolocation_service.dart  # GPS tracking + multi-sample best-accuracy
    geofencing_service.dart   # Radius evaluation + car speed detection
    notification_service.dart # Push notifications (web-safe)
    storage_service.dart      # localStorage persistence layer
    geocoding_service.dart    # Address → coordinates
    place_search_service.dart # Nominatim autocomplete with proximity sorting
  utils/
    haversine.dart           # Distance calculation
  widgets/
    radius_slider.dart       # Geofence radius control
    store_card.dart          # Store list item
web/
  index.html                 # PWA entry with meta tags + loading screen
  manifest.json              # PWA manifest (name, icons, theme)
  icons/                     # App icons (192, 512, maskable)
```
