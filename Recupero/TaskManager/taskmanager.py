class TaskManager:

    def __init__(self, tasks:dict[str, dict[str, str | bool]]={}) -> None:

        self.tasks:dict[str, dict[str, str | bool]] = tasks

    def create_task(self, task_id:str, descrizione:str) -> dict | str:
        
        if task_id in self.tasks:

            return "Errore: task esiste già"
        
        else:
            self.tasks[task_id] = {"descrizione" : descrizione, "completato" : False}

            return self.tasks[task_id]
        
    def complete_task(self, task_id:str) -> dict[str, dict[str, str | bool]] | str:

        if task_id in self.tasks:

            self.tasks[task_id]["completato"] = True 

            return {task_id : self.tasks[task_id]}
        
        else:

            return "Chiave non presente!"
        
    def update_description(self, task_id:str, nuova_descrizione:str) -> dict[str, dict[str, str | bool]] | str:

        if task_id in self.tasks:

            return "Task non presente"

        else:

            self.tasks[task_id]["descrizione"] = nuova_descrizione
            return {task_id: self.tasks[task_id]}
        
    def remove_task(self, task_id:str) -> dict | str:

        if task_id not in self.tasks:

            return "Task non presente!" 
        
        else:
            
            value = self.tasks.pop(task_id)

            return {task_id : value}
        
    def list_tasks(self) -> list[str]:

        return list(self.tasks.keys())
    
    def get_task(self, task_id:str) -> dict | str:

        if task_id not in self.tasks:

            return "Errore task non presente"
        
        else:

            return {task_id : self.tasks[task_id]}
