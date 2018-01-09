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
Registers a decomposition for controlled Ry gates.

It uses 1 controlled Rz, 2 Hadamards, 1 S, and 1 S^\dagger.
"""

import math

from projectq.cengines import DecompositionRule
from projectq.meta import get_control_count
from projectq.ops import Ry, Rz, H, S, Sdag, C


def _decompose_CRy(cmd):
    """ Decompose the controlled Ry gate (into controlled Rz, H, and S)."""
    qubit = cmd.qubits[0]
    ctrl = cmd.control_qubits
    gate = cmd.gate
    n = get_control_count(cmd)

    
    Sdag | qubit
    H | qubit
    C(Rz(gate.angle), n) | (ctrl, qubit)
    H | qubit
    S | qubit


def _recognize_CRy(cmd):
    """ Recognize the controlled Rz gate. """
    return get_control_count(cmd) >= 1


all_defined_decomposition_rules = [
    DecompositionRule(Ry, _decompose_CRy, _recognize_CRy)
]
