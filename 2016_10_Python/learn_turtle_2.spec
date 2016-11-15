# -*- mode: python -*-

block_cipher = None


a = Analysis(['learn_turtle_2.py'],
             pathex=['D:\\#学习+工作文档\\GitHub\\LearnToProgram\\2016_10_Python'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='learn_turtle_2',
          debug=False,
          strip=False,
          upx=True,
          console=True )
