function favoriteMatch(button) {
    const matchId = button.getAttribute("data-match-id");
    const summonerName = button.getAttribute("data-summoner-name");
    const map = button.getAttribute("data-map");
    const championPlayed = button.getAttribute("data-champion-played");
    const victoryOrDefeat = button.getAttribute("data-victory-or-defeat");
    const kda = button.getAttribute("data-kda");

    fetch(`/favorite/?match_id=${matchId}&summoner_name=${summonerName}&map=${map}&champion_played=${championPlayed}&victory_or_defeat=${victoryOrDefeat}&kda=${kda}`, {
        method: "POST",
    })
    .then((response) => response.json())
    .then((data) => {
        alert(data.message);
    })
    .catch((error) => {
        console.error("Erro ao favoritar a partida:", error);
    });
}

function deleteMatch(matchId, summonerName) {
    fetch(`/delete/?match_id=${matchId}&summoner_name=${summonerName}`, {
        method: "DELETE",
    })
    .then((response) => response.json())
    .then((data) => {
        alert(data.message);
        const rowToRemove = document.getElementById(`match-row-${matchId}`);
        if (rowToRemove) {
            rowToRemove.remove();
        }
    })
    .catch((error) => {
        console.error("Erro ao deletar a partida:", error);
    });
}

function confirmDelete(matchId, summonerName) {
    const confirmation = confirm("Are you sure you want to delete this match from favorites?");
    
    if (confirmation) {
        deleteMatch(matchId, summonerName);
    }
}

function viewFavorites(summonerName) {
    window.location.href = `/favorites/${summonerName}`;
}

document.getElementById("back-to-matches").addEventListener("click", function() {
    window.history.back();
});
