from flask import Blueprint, render_template, jsonify, abort, redirect, flash

class Router(Blueprint):

    def __init__(self, name, import_name, static_folder=None, static_url_path=None, template_folder=None, url_prefix=None, subdomain=None, url_defaults=None, root_path=None, cli_group=...):
        super().__init__(name, import_name, static_folder, static_url_path, template_folder, url_prefix, subdomain, url_defaults, root_path, cli_group)
    
    def send_resp(self, type, resp, **context):  
        if type == 'json':
            return jsonify(resp)
        elif type == 'html':
            return render_template(resp, **context)
        elif type == 'code':
            return abort(resp)
        elif type == 'redirect':
            return redirect(resp)
        else:
            return resp

    def flash_message(message, category='message'):
        flash(message, category)
