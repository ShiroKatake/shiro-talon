from talon import Module, Context, actions

mod = Module()

mod.apps.fellowship = r"""
os: windows
and app.name: fellowship
"""

ctx = Context()
ctx.matches = r"""
app: fellowship
"""


@ctx.action_class("user")
class UserActions:
    def foot_switch_top_down():
        """Start move"""
        actions.user.mouse_release_held_buttons()
        actions.key("w:down")

    def foot_switch_top_up(held: bool):
        """Stop move"""
        actions.key("w:up")

    def foot_switch_center_down():
        """Start stand still"""
        mouse_click(0)
        mouse_click(1)
        actions.mouse_drag(0)
        actions.mouse_drag(1)

    def foot_switch_center_up(held: bool):
        """Stop stand still"""
        actions.user.mouse_drag_end()

    def foot_switch_left_down():
        """Toggle voice chat for game"""

    def foot_switch_left_up(held: bool):
        """Toggle voice chat for game"""

    def foot_switch_right_down():
        """Toggle voice chat for game"""

    def foot_switch_right_up(held: bool):
        """Toggle voice chat for game"""

def mouse_click(button: int):
    actions.mouse_click(button)