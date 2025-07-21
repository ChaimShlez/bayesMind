from dal.connectionWrapper import ConnectionWrapper


class Queries:

    def __init__(self):
        self._connection=ConnectionWrapper()

    def create_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS model_probabilities (
                id INT AUTO_INCREMENT PRIMARY KEY,
                feature_name VARCHAR(255),
                feature_value VARCHAR(255),
                label VARCHAR(255),
                probability FLOAT
            );
            """
    def save_modal(self,agent):
        # print(agent.status.name)
        # s=str(agent.status)
        sql=("INSERT INTO agents (codeName,realName,location,status,missionsCompleted)"
             " VALUES (%s,%s,%s,%s,%s)")

        parameters = (
            agent.codeName,
            agent.realName,
            agent.location,
           agent.status,
            agent.missionsCompleted
        )
        print(agent.status)
        self._connection.execute(sql, parameters)



    def deleteByCodeName(self,codeNmae):
        sql = "DELETE  FROM agents WHERE codeName =%s"

        parameters = (
            codeNmae,)
        self._connection.execute(sql,parameters)

    def updateById(self, id, agent):
        sql = "UPDATE agents SET codeName = %s,realName = %s,location = %s, status = %s, missionsCompleted = %s WHERE id = %s"
        parameters = (agent.codeName,
                      agent.realName,
                      agent.location,
                      agent.status,
                      agent.missionsCompleted,
                      id)
        self._connection.execute(sql, parameters)













