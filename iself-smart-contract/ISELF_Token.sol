// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title HUMANSELF (ISELF) - Accountability Token
 * @dev Questo è un "Soulbound Token" (SBT). Non è trasferibile né vendibile.
 * Serve esclusivamente come layer di tracciabilità per l'ecosistema Humansafe.
 * Certifica: Azioni preventive, superamento audit cognitivi, empatia sociale.
 */

contract ISELF_Token {
    string public name = "Humanself Accountability Token";
    string public symbol = "ISELF";
    
    address public humansafeSystemAdmin;

    // Mappatura che associa l'indirizzo dell'utente al suo "Credito Formativo"
    mapping(address => uint256) public preventiveCredits;

    // Eventi registrati pubblicamente e in modo immutabile sulla blockchain
    event EvolutionRewarded(address indexed user, uint256 amount, string reason);
    event TransferAttemptBlocked(address indexed from, address indexed to);

    constructor() {
        humansafeSystemAdmin = msg.sender; // Il sistema Humansafe governa l'emissione
    }

    // Solo i facilitatori certificati Humansafe possono validare e coniare il token
    modifier onlyAdmin() {
        require(msg.sender == humansafeSystemAdmin, "Azione non autorizzata. Solo Humansafe puo certificare l'evoluzione.");
        _;
    }

    /**
     * @dev Eroga ISELF a una "Cellula" che ha completato un'azione di disintossicazione
     * o ha superato un Audit B2B.
     */
    function rewardCell(address _cellAddress, uint256 _amount, string memory _reason) public onlyAdmin {
        preventiveCredits[_cellAddress] += _amount;
        emit EvolutionRewarded(_cellAddress, _amount, _reason);
    }

    /**
     * @dev FUNZIONE SOULBOUND: Blocca qualsiasi tentativo di vendita o trasferimento.
     * La consapevolezza e la sicurezza cognitiva non si possono comprare, si conquistano.
     */
    function transfer(address _to, uint256 _amount) public returns (bool) {
        emit TransferAttemptBlocked(msg.sender, _to);
        revert("Trasferimento negato: ISELF e' un token legato alla tua identita' (Soulbound). Non ha valore speculativo.");
    }
}
