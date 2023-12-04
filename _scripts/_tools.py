# -*- coding: utf-8 -*-
"""."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

_RESOURCES = BASE_DIR.parent.joinpath('_resources', 'resources.qrc')


def compile_resources(output: Path, input: Path = None) -> None:
    if input:
        cmd = f'pyside6-rcc "{input}" -o "{output}"'
    else:
        cmd = f'pyside6-rcc "{_RESOURCES}" -o "{output}"'
    subprocess.run(
        args=cmd,
        shell=True,
        check=True,
    )


def compile_ui_file(ui_dir: Path) -> None:
    for file in ui_dir.rglob('*.ui'):
        if file.is_file() and file.suffix == '.ui':
            filename = f'Ui_{file.stem}.py'
            subprocess.run(
                args=f'pyside6-uic "{file}" -o "{file.parent.joinpath(filename)}"',
                shell=True,
                check=True,
            )


def create_or_update_translation(app_id, langs: list, path: Path, shell: bool = True) -> None:
    for lang in langs:
        output = path.joinpath('i18n', f'{app_id}_{lang}.ts')
        output.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            args=f'pyside6-lupdate -extensions "ui,qml,py" "{path}" -ts "{output}"',
            shell=shell,
            check=True,
        )


def compile_translation(path: Path, shell: bool = True) -> None:
    for file in path.rglob('*.ts'):
        if file.is_file() and file.suffix == '.ts':
            output = path.joinpath('i18n', f'{file.stem}.qm')
            output.parent.mkdir(parents=True, exist_ok=True)
            subprocess.run(
                args=f'pyside6-lrelease "{file}" "{output}"',
                shell=shell,
                check=True,
            )


if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent
    RESOURCES_QRC = BASE_DIR.parent.joinpath('_resources', 'resources.qrc')
    RESOURCES_RC_PY = BASE_DIR.joinpath('resources_rc.py')

    compile_resources(output=RESOURCES_RC_PY)
    # compile_ui_file(ui_dir=BASE_DIR)
    # create_or_update_translation(
    #     app_id='teste',
    #     langs=['en_US'],
    #     path=BASE_DIR,
    # )
    # compile_translation(
    #     BASE_DIR,
    # )
