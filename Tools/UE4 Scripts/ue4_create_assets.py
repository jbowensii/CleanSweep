import unreal
import os

script_dir = r'C:\Unreal Projects\Moria\Tools\UE4 Scripts'
input_file = os.path.join(script_dir, 'objects to create.txt')
source_fbx = os.path.join(script_dir, 'Debris.fbx')
log_file = os.path.join(script_dir, 'import_log.txt')

log_lines = []

def log(msg):
    unreal.log(msg)
    log_lines.append(msg)

with open(input_file, 'r') as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

if len(lines) < 2:
    log('ERROR: objects to create.txt must have at least 2 lines (path + asset names).')
else:
    destination_path = lines[0]
    asset_names = lines[1:]

    log('Destination: ' + destination_path)
    log('Assets to create: ' + str(len(asset_names)))

    if not destination_path.startswith('/Game/'):
        log('ERROR: Destination path must start with /Game/ e.g. /Game/Art/Assets/Kits/Deco/MyFolder')
    elif not os.path.exists(source_fbx):
        log('ERROR: Debris.fbx not found at: ' + source_fbx)
    else:
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        task_list = []

        for name in asset_names:
            task = unreal.AssetImportTask()
            task.filename = source_fbx
            task.destination_path = destination_path
            task.destination_name = name
            task.replace_existing = True
            task.automated = True
            task.save = True
            options = unreal.FbxImportUI()
            options.import_mesh = True
            options.import_textures = False
            options.import_materials = False
            options.import_as_skeletal = False
            options.static_mesh_import_data.combine_meshes = True
            task.options = options
            task_list.append(task)
            log('Queued: ' + name)

        log('Importing...')
        asset_tools.import_asset_tasks(task_list)

        success = 0
        failed = 0
        for task in task_list:
            if task.imported_object_paths:
                log('  IMPORTED: ' + task.destination_name)
                success += 1
            else:
                log('  FAILED:   ' + task.destination_name)
                failed += 1

        log('Done! Success: ' + str(success) + '  Failed: ' + str(failed))

with open(log_file, 'w') as f:
    f.write('\n'.join(log_lines))

unreal.log('Log written to: ' + log_file)
