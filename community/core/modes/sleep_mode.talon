mode: sleep
-
settings():
    # Stop continuous scroll/gaze scroll with a pop
    user.mouse_enable_pop_stops_scroll = false
    # Stop pop click with 'control mouse' mode
    user.mouse_enable_pop_click = 0
    # Stop mouse scroll down using hiss noise
    user.mouse_enable_hiss_scroll = false

parrot(cluck):
    app.notify("talon wake")
    user.mouse_wake()
    user.talon_mode()
    user.mouse_enable_pop_click = 0
    tracking.control_toggle()
