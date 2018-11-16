import smartsheet
import re

ss_client = smartsheet.Smartsheet('l07xoamqp4rg0v9helj4talqy2')
user_profile = ss_client.Users.get_current_user().to_dict()
print(user_profile)
response = ss_client.Workspaces.list_workspaces(include_all=True)
workspaces = response.data

for ws in workspaces:
    workspace = ss_client.Workspaces.get_workspace(ws.id_)
    result = re.match("^(?P<jobnumber>[0-9]{4}-[0-9]{5})",workspace.name)
    if result and result.group('jobnumber'):
        job_number = result.group('jobnumber')
        print(job_number)
        if job_number == '2018-99999':
            for sheet in workspace.sheets:
                updated_sheet = ss_client.Sheets.update_sheet(
                        sheet.id_,
                        ss_client.models.Sheet({
                            'name': job_number + ' ' + sheet.name
                        }) )