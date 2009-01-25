# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/options_renaming.ui'
#
# Created: Sun Jan 25 20:55:41 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_RenamingOptionsPage(object):
    def setupUi(self, RenamingOptionsPage):
        RenamingOptionsPage.setObjectName("RenamingOptionsPage")
        RenamingOptionsPage.resize(892, 693)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RenamingOptionsPage.sizePolicy().hasHeightForWidth())
        RenamingOptionsPage.setSizePolicy(sizePolicy)
        self.vboxlayout = QtGui.QVBoxLayout(RenamingOptionsPage)
        self.vboxlayout.setObjectName("vboxlayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(RenamingOptionsPage)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.rename_files = QtGui.QCheckBox(RenamingOptionsPage)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rename_files.sizePolicy().hasHeightForWidth())
        self.rename_files.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.rename_files.setFont(font)
        self.rename_files.setObjectName("rename_files")
        self.horizontalLayout.addWidget(self.rename_files)
        self.vboxlayout.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(RenamingOptionsPage)
        self.line.setFrameShadow(QtGui.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.vboxlayout.addWidget(self.line)
        self.ascii_filenames = QtGui.QCheckBox(RenamingOptionsPage)
        self.ascii_filenames.setObjectName("ascii_filenames")
        self.vboxlayout.addWidget(self.ascii_filenames)
        self.windows_compatible_filenames = QtGui.QCheckBox(RenamingOptionsPage)
        self.windows_compatible_filenames.setObjectName("windows_compatible_filenames")
        self.vboxlayout.addWidget(self.windows_compatible_filenames)
        self.groupBox = QtGui.QGroupBox(RenamingOptionsPage)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.file_naming_format = QtGui.QTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_naming_format.sizePolicy().hasHeightForWidth())
        self.file_naming_format.setSizePolicy(sizePolicy)
        self.file_naming_format.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.file_naming_format.setFont(font)
        self.file_naming_format.setProperty("cursor", QtCore.QVariant(QtCore.Qt.IBeamCursor))
        self.file_naming_format.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.file_naming_format.setTabStopWidth(20)
        self.file_naming_format.setAcceptRichText(True)
        self.file_naming_format.setObjectName("file_naming_format")
        self.verticalLayout_4.addWidget(self.file_naming_format)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.renaming_error = QtGui.QLabel(self.groupBox)
        self.renaming_error.setAlignment(QtCore.Qt.AlignCenter)
        self.renaming_error.setObjectName("renaming_error")
        self.horizontalLayout_2.addWidget(self.renaming_error)
        self.file_naming_format_default = QtGui.QPushButton(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.file_naming_format_default.sizePolicy().hasHeightForWidth())
        self.file_naming_format_default.setSizePolicy(sizePolicy)
        self.file_naming_format_default.setMinimumSize(QtCore.QSize(0, 0))
        self.file_naming_format_default.setObjectName("file_naming_format_default")
        self.horizontalLayout_2.addWidget(self.file_naming_format_default)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.vboxlayout.addWidget(self.groupBox)
        self.use_va_format = QtGui.QGroupBox(RenamingOptionsPage)
        self.use_va_format.setFlat(False)
        self.use_va_format.setCheckable(True)
        self.use_va_format.setObjectName("use_va_format")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.use_va_format)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.va_file_naming_format = QtGui.QTextEdit(self.use_va_format)
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(10)
        self.va_file_naming_format.setFont(font)
        self.va_file_naming_format.setProperty("cursor", QtCore.QVariant(QtCore.Qt.IBeamCursor))
        self.va_file_naming_format.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.va_file_naming_format.setTabStopWidth(20)
        self.va_file_naming_format.setAcceptRichText(True)
        self.va_file_naming_format.setObjectName("va_file_naming_format")
        self.hboxlayout.addWidget(self.va_file_naming_format)
        self.verticalLayout_3.addLayout(self.hboxlayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.renaming_va_error = QtGui.QLabel(self.use_va_format)
        self.renaming_va_error.setAlignment(QtCore.Qt.AlignCenter)
        self.renaming_va_error.setObjectName("renaming_va_error")
        self.horizontalLayout_3.addWidget(self.renaming_va_error)
        self.va_copy_from_above = QtGui.QPushButton(self.use_va_format)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.va_copy_from_above.sizePolicy().hasHeightForWidth())
        self.va_copy_from_above.setSizePolicy(sizePolicy)
        self.va_copy_from_above.setMinimumSize(QtCore.QSize(0, 0))
        self.va_copy_from_above.setObjectName("va_copy_from_above")
        self.horizontalLayout_3.addWidget(self.va_copy_from_above)
        self.va_file_naming_format_default = QtGui.QPushButton(self.use_va_format)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.va_file_naming_format_default.sizePolicy().hasHeightForWidth())
        self.va_file_naming_format_default.setSizePolicy(sizePolicy)
        self.va_file_naming_format_default.setMinimumSize(QtCore.QSize(0, 0))
        self.va_file_naming_format_default.setObjectName("va_file_naming_format_default")
        self.horizontalLayout_3.addWidget(self.va_file_naming_format_default)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.vboxlayout.addWidget(self.use_va_format)
        self.groupBox_2 = QtGui.QGroupBox(RenamingOptionsPage)
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.example_filename = QtGui.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.example_filename.setFont(font)
        self.example_filename.setFrameShape(QtGui.QFrame.NoFrame)
        self.example_filename.setFrameShadow(QtGui.QFrame.Plain)
        self.example_filename.setLineWidth(1)
        self.example_filename.setTextFormat(QtCore.Qt.RichText)
        self.example_filename.setWordWrap(True)
        self.example_filename.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.example_filename.setObjectName("example_filename")
        self.verticalLayout.addWidget(self.example_filename)
        self.vboxlayout.addWidget(self.groupBox_2)

        self.retranslateUi(RenamingOptionsPage)
        QtCore.QMetaObject.connectSlotsByName(RenamingOptionsPage)

    def retranslateUi(self, RenamingOptionsPage):
        RenamingOptionsPage.setWindowTitle(_("Form"))
        self.label.setText(_("File naming"))
        self.rename_files.setText(_("Enabled"))
        self.ascii_filenames.setText(_("Replace non-ASCII characters"))
        self.windows_compatible_filenames.setText(_("Replace Windows-incompatible characters"))
        self.groupBox.setTitle(_("Name files like this"))
        self.file_naming_format.setHtml(QtGui.QApplication.translate("RenamingOptionsPage", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Monospace\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.file_naming_format_default.setText(_("Default"))
        self.use_va_format.setTitle(_("Name compilations differently"))
        self.va_copy_from_above.setText(_("Copy from above"))
        self.va_file_naming_format_default.setText(_("Default"))
        self.groupBox_2.setTitle(_("Examples"))
        self.example_filename.setText(_("fasdfasdfasdfasdfasdfsdfasfd"))

