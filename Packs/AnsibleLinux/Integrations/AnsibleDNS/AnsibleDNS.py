import demistomock as demisto  # noqa: F401
import ssh_agent_setup

# Import Generated code
from AnsibleApiModule import *  # noqa: E402
from CommonServerPython import *  # noqa: F401

host_type = "local"

# MAIN FUNCTION


def main() -> None:
    """main function, parses params and runs command functions

    :return:
    :rtype:
    """

    # SSH Key integration requires ssh_agent to be running in the background
    ssh_agent_setup.setup()

    # Common Inputs
    command = demisto.command()
    args = demisto.args()
    int_params = demisto.params()
    creds_mapping = {"identifier": "key_name", "password": "key_secret"}

    try:
        if command == "test-module":
            # This is the call made when pressing the integration Test button.
            return_results(
                "This integration does not support testing from this screen. \
                           Please refer to the documentation for details on how to perform \
                           configuration tests."
            )
        elif command == "dns-nsupdate":
            return_results(generic_ansible("DNS", "nsupdate", args, int_params, host_type, creds_mapping))
    # Log exceptions and return errors
    except Exception as e:
        return_error(f"Failed to execute {command} command.\nError:\n{e!s}")


# ENTRY POINT


if __name__ in ("__main__", "__builtin__", "builtins"):
    main()
