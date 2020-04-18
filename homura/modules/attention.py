from typing import Tuple, Optional

import torch
from torch import nn

from .functional.attention import kv_attention


class KeyValAttention(nn.Module):
    def __init__(self,
                 scaling: bool = False,
                 dropout_prob: float = 0):
        super(KeyValAttention, self).__init__()
        self._scaling = scaling
        self._dropout = dropout_prob

    def forward(self,
                query: torch.Tensor,
                key: torch.Tensor,
                value: torch.Tensor,
                mask: Optional[torch.Tensor] = None,
                additive_mask: Optional[torch.Tensor] = None,
                ) -> Tuple[torch.Tensor, torch.Tensor]:
        return kv_attention(query, key, value, mask, additive_mask,
                            self.training, self._dropout, self._scaling)

