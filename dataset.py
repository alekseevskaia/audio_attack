from typing import Tuple
from torch.utils.data import Dataset
from pathlib import Path
import torchaudio
from torch import Tensor

class AudioDataset(Dataset):
    def __init__(self, root: Path) -> None:
        self.root = root
        self.audio_files = sorted(Path(self.root).glob("*.wav"), key=lambda item: item.name)

    def __len__(self) -> int:
        return len(self.audio_files)

    def __getitem__(self, index: int) -> Tuple[Tensor, str]:
        return self.load_item(self.audio_files[index])
    
    def load_item(self, file: str) -> Tuple[Tensor, str]:
        waveform, sample_rate = torchaudio.load(file)
        return waveform, sample_rate