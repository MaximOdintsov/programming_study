import time
import pyautogui

# text = input('text: ')
text = """def handle(self, *args, **opts):
        root = Path(opts['root'])
        workspace_id = opts['workspace_id']
        path_workspace = root / str(workspace_id) if workspace_id else Path(root.parent, root.stem)
        clean_dir(path_workspace)
        print('path_workspace', path_workspace)
        if path_workspace.with_suffix('.zip').exists():
            shutil.unpack_archive(
                path_workspace.with_suffix('.zip'), path_workspace)
        else:
            raise FileNotFoundError(f'No such workspace found: {workspace_id}')
        if opts['light']:
            if workspace_exists(path_workspace / 'workspace.json'):
                print('Launched with light option. Workspace found. Skipping...')
                clean_dir(path_workspace)
                return
        version_file = Path(path_workspace / 'version.txt')
        version = version_file.read_text() if version_file.exists() else opts.get('use_version', '1.6.0')
        if opts.get('users'):
            load_object(None, path_workspace / 'users.json', 'users')
        ws = load_object(None, path_workspace / 'workspace.json', 'workspace')
        if opts.get('fieldtypes'):
            load_object(ws, path_workspace / 'fieldtypes.json', 'fieldtypes')
        if opts.get('doctypes'):
            for path in (path_workspace / 'doctypes').iterdir():
                dtype = load_object(ws, path / 'doctype.json', 'doctype')
                load_object(dtype, path / 'blocks.json', 'blocks')
                load_object(dtype, path / 'fields.json', 'fields')
                dtype = fix_doctype_order(dtype)
                if dtype is None:
                    print("No dtype: {}".format(dtype))
                else:
                    dtype.save()

            nb_models_path = path_workspace / 'models' / 'doctype' / 'nb_classifiers'
            target_models_path = Path('../../data/models/')
            if nb_models_path.exists():
                for file in nb_models_path.iterdir():
                    old_data = read_pickle(file)
                    guid = file.stem
                    ws_ = Workspace.objects.filter(guid=guid)
                    if ws_.exists():
                        ws_ = ws_[0]
                        new_data = reformat_nb_models(old_data)
                        write_pickle(
                            target_models_path / 'doctype' / 'nb_classifiers' /
                            f'nb_{ws_.id}.pickle', new_data
                        )
                    else:
                        print(f'No workspace found: {guid}')
            s2_models_path = path_workspace / 'models' / 's2'
            if s2_models_path.exists():
                for path in s2_models_path.iterdir():
                    dtype = DocType.objects.filter(guid=path.name).first()
                    if dtype:
                        copy_s2_models(path, target_models_path /
                                       's2' / str(dtype.id), dtype)

        if opts.get('projects'):
            if version < '1.6.7':
                project_path = path_workspace
            else:
                project_path = path_workspace / 'projects'

            for path in project_path.iterdir():
                if path.is_dir() and (path / 'project.json').exists():
                    pj = load_object(ws, path / 'project.json', 'project')
                    load_object(pj, path / 'user_permissions.json', 'user_permissions')
                    if opts.get('files') and (path / 'files').exists():
                        for file in tqdm((path / 'files').iterdir(), desc='files'):
                            print(f'file: {file}...')
                            if file.is_file() and file.name.endswith('.json'):
                                loaded_file = load_object(pj, file, 'file')
                                print(f'loaded file: {loaded_file}...')
                                if opts.get('copy'):
                                    file_suffix = loaded_file.file.name.split('.')[-1]
                                    file_name = f'{file.stem}.{file_suffix}'

                                    file_path = (path / 'files' / 'files')
                                    if (file_path / file_name).exists():
                                        print(f'copy file: {file_path / file_name} to: {loaded_file.file.path}...')
                                        copy_file(file_path / file_name, loaded_file.file.path) # file.pdf to file.pdf

                                        if loaded_file.pdf:
                                            json_name = file_name.split('.')[0] + '.json'

                                            print(f'copy file: {file_path / f"{file_name}.pdf"} to: {loaded_file.pdf.path}...')
                                            copy_file(file_path / f'{file_name}.pdf', loaded_file.pdf.path) # file.pdf.pdf to file.pdf.pdf

                                            print(f'copy file: {path / "files" / json_name} to: {f"{loaded_file.pdf.path}.json"}')
                                            copy_file(path/ 'files' / json_name, f'{loaded_file.pdf.path}.json') # file.json to file.pdf.json
                    if opts.get('documents') and (path / 'documents').exists():
                        for file in tqdm((path / 'documents').iterdir(), desc='documents'):
                            load_object(pj, file, 'document')
        clean_dir(path_workspace)
"""
time.sleep(5)


for char in text:
    if char in ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', ':', '"', '|', '<', '>', '?']:
        pyautogui.keyDown('shift')
        pyautogui.write(char)
        pyautogui.keyUp('shift')
    else:
        pyautogui.write(char)