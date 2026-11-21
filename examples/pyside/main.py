"""Exemple PySide6 avec clem2k-ui.

    pip install "clem2k-ui[qt] @ git+https://github.com/clem2k/clem2k-ui"
    python main.py           # ou: python main.py hc
Installe JetBrains Mono sur le système pour la bonne police (sinon repli monospace).
"""
import sys

from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel, QLineEdit, QListWidget,
                               QMainWindow, QProgressBar, QPushButton, QVBoxLayout, QWidget)

import clem2k_ui


def main() -> None:
    app = QApplication(sys.argv)
    clem2k_ui.apply_qt(app, sys.argv[1] if len(sys.argv) > 1 else "dark")

    win = QMainWindow()
    win.setWindowTitle("vision — conteneurs")
    root = QWidget()
    layout = QHBoxLayout(root)

    side = QListWidget()
    side.addItems(["vision", "proxmox", "terminal", "réglages"])
    side.setFixedWidth(200)
    side.setCurrentRow(0)
    layout.addWidget(side)

    main_col = QVBoxLayout()
    title = QLabel("> conteneurs")
    title.setProperty("role", "h1")
    main_col.addWidget(title)
    hint = QLabel("3 services, 1 à surveiller")
    hint.setProperty("role", "muted")
    main_col.addWidget(hint)
    main_col.addWidget(QLineEdit(placeholderText="Filtrer…"))
    main_col.addWidget(QCheckBox("Redémarrage auto"))
    bar = QProgressBar()
    bar.setValue(64)
    main_col.addWidget(bar)
    buttons = QHBoxLayout()
    deploy = QPushButton("Déployer")
    deploy.setProperty("variant", "primary")
    delete = QPushButton("Supprimer")
    delete.setProperty("variant", "danger")
    buttons.addWidget(deploy)
    buttons.addWidget(QPushButton("Annuler"))
    buttons.addStretch()
    buttons.addWidget(delete)
    main_col.addLayout(buttons)
    main_col.addStretch()
    layout.addLayout(main_col)

    win.setCentralWidget(root)
    win.statusBar().showMessage("● connecté à vision.local")
    win.resize(820, 480)
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
