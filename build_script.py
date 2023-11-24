import PyInstaller.__main__

PyInstaller.__main__.run([
    'frame_extractor.py',  # Sostituisci con il nome del tuo script principale
    '--onefile',
    '--windowed',
    '--name=FrameExtractor',  # Sostituisci con il nome desiderato per l'app
])
