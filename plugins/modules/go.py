# # main_app.py
# import go_bridge  # Import the module you just created

# def main():
#     print("Attempting to call Go function from main_app.py...")
#     data = go_bridge.call_crud_project()

#     if data:
#         print("\nSuccessfully received data in main_app.py:")
#         print(data)
#     else:
#         print("\nFailed to get data from Go function in main_app.py.")

# if __name__ == '__main__':
#     main()
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.terraform.go.plugins.module_utils.go_bridge import call_crud_project


def main():
   module = AnsibleModule(
       argument_spec=dict(
           action=dict(type='str', required=False, default="list")
       )
   )

   action = module.params['action']
   result = {"changed": False, "action": action}

   try:
       if action == "list":
           output = call_crud_project()
           result["changed"] = True
           result["message"] = "Projects listed successfully"
           result["output"] = output
       else:
           module.fail_json(msg=f"Invalid action: {action}. Only 'list' is supported.", **result)

       module.exit_json(**result)

   except Exception as e:
       module.fail_json(msg=str(e), **result)

if __name__ == '__main__':
   main()
