#!/usr/bin/python3
"""Module for the command-line interpreter."""
import cmd

class HBNBCommand(cmd.Cmd):
    """Command-line interpreter for AirBnB clone project."""

    def do_create(self, arg):
        """Create a new instance of a specified class."""
        pass

    def do_show(self, arg):
        """Show information about a specified instance."""
        pass

    # Other command methods (e.g., do_update, do_destroy, etc.)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
