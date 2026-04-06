from talon import Module, actions

mod = Module()
apps = mod.apps
apps.microsoft_teams = r"""
os: windows
and app.name: /teams/
os: windows
and app.name: /Teams/
"""

@mod.action_class
class Actions:
    def teams_mute():
        """Toggle Teams voice settings"""
        actions.key("ctrl-shift-alt-m")