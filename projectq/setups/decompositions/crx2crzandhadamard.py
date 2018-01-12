#   Copyright 2017 ProjectQ-Framework (www.projectq.ch)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""
Registers a decomposition for controlled Rx gates.

It uses 1 controlled Rz and 2 Hadamards.
"""

import math

from projectq.cengines import DecompositionRule
from projectq.meta import get_control_count
from projectq.ops import Rx, Rz, H, C


def _decompose_CRx(cmd):
    """ Decompose the controlled Rx gate (into controlled Rz and H)."""
    qubit = cmd.qubits[0]
    ctrl = cmd.control_qubits
    gate = cmd.gate
    n = get_control_count(cmd)

    H | qubit
    C(Rz(gate.angle), n) | (ctrl, qubit)
    H | qubit


def _recognize_CRx(cmd):
    """ Recognize the controlled Rx gate. """
    return get_control_count(cmd) >= 1


all_defined_decomposition_rules = [
    DecompositionRule(Rx, _decompose_CRx, _recognize_CRx)
]
