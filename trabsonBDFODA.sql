CREATE TABLE `Tarefas` (
  `Descrição` varchar(100) NOT NULL,
  `Prioridade` int(11) NOT NULL,
  `Data` datetime NOT NULL,
  `Id` int(11) NOT NULL AUTO_INCREMENT,
  `Concluído` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8
