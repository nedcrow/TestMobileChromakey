import unreal

texture_jpg = 'C:/Users/HARIM/Pictures/selfiesample.JPG'


def importMyAssets():
    texture_task = buildImportTask(texture_jpg, '/Game/Textures')
    executeImportTasks([texture_task])


def buildImportTask(filename, destination_path):
    task = unreal.AssetImportTask()
    task.set_editor_property('automated', True)
    task.set_editor_property('destination_name', 'Test')
    task.set_editor_property('destination_path', destination_path)
    task.set_editor_property('filename', filename)
    task.set_editor_property('replace_existing', False)
    task.set_editor_property('save', False)
    return task


def executeImportTasks(tasks):
    unreal.AssetToolsHelpers.get_asset_tools().import_asset_tasks(tasks)
    print('imported Task(s)')


def talk():
    print('talk three')


if __name__ == '__main__':
    print('Imported main.py')
