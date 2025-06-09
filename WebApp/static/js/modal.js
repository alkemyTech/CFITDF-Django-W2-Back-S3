function openActionModal(actionUrl, entityName, actionType) {
    var modalLabel = document.getElementById('confirmActionModalLabel');
    var modalMessage = document.getElementById('modalMessage');
    var modalHeader = document.getElementById('modalHeader');
    var modalActionBtn = document.getElementById('modalActionBtn');

    if (actionType === 'delete') {
      modalLabel.textContent = "Confirmar eliminación";
      modalMessage.textContent = "¿Está seguro que desea desactivar " + entityName + "?";
      modalHeader.classList.add("bg-danger", "text-white");
      modalActionBtn.classList.add("btn-danger");
      modalActionBtn.textContent = "Eliminar";
    } else {
      modalLabel.textContent = "Confirmar restauración";
      modalMessage.textContent = "¿Está seguro que desea restaurar " + entityName + "?";
      modalHeader.classList.add("bg-success", "text-white");
      modalActionBtn.classList.add("btn-success");
      modalActionBtn.textContent = "Restaurar";
    }

    document.getElementById('modalActionBtn').setAttribute('href', actionUrl);
    var actionModal = new bootstrap.Modal(document.getElementById('confirmActionModal'));
    actionModal.show();
}