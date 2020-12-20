-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:8081
-- Généré le : Dim 20 déc. 2020 à 14:04
-- Version du serveur :  5.7.24
-- Version de PHP : 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `breizhibus`
--
CREATE DATABASE IF NOT EXISTS `breizhibus` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `breizhibus`;

-- --------------------------------------------------------

--
-- Structure de la table `arrets`
--

DROP TABLE IF EXISTS `arrets`;
CREATE TABLE `arrets` (
  `id_arret` int(11) NOT NULL,
  `nom` varchar(20) NOT NULL,
  `adresse` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `arrets`
--

INSERT INTO `arrets` (`id_arret`, `nom`, `adresse`) VALUES
(1, 'Korrigan', '1 impasse du Korrigan'),
(2, 'Morgana', '2 place Morgana'),
(3, 'L\'Ankou', '3 place du l\'Ankou'),
(4, 'Ys', '4 rue de l\'ile d\'Ys'),
(5, 'Viviane', '5 avenue de Viviane'),
(6, 'Guénolé', '6 rue Saint Guénolé');

-- --------------------------------------------------------

--
-- Structure de la table `arret_ligne`
--

DROP TABLE IF EXISTS `arret_ligne`;
CREATE TABLE `arret_ligne` (
  `id_ligne` int(11) NOT NULL,
  `id_arret` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `arret_ligne`
--

INSERT INTO `arret_ligne` (`id_ligne`, `id_arret`) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 2),
(2, 4),
(2, 6),
(3, 4),
(3, 5),
(3, 6),
(3, 1),
(4, 1),
(4, 3),
(4, 5);

-- --------------------------------------------------------

--
-- Structure de la table `bus`
--

DROP TABLE IF EXISTS `bus`;
CREATE TABLE `bus` (
  `id_bus` int(11) NOT NULL,
  `numero` varchar(4) NOT NULL,
  `immatriculation` varchar(7) NOT NULL,
  `nombre_place` int(11) NOT NULL,
  `id_ligne` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `bus`
--

INSERT INTO `bus` (`id_bus`, `numero`, `immatriculation`, `nombre_place`, `id_ligne`) VALUES
(1, 'BB01', 'CA123DO', 20, 1),
(2, 'BB02', 'NO123EL', 30, 2),
(3, 'BB03', 'JE123UX', 20, 3),
(4, 'BB04', 'RE123PA', 30, 1),
(5, 'BB05', 'PU123LL', 30, 4),
(6, 'BB06', 'JO123EL', 30, 4),
(7, 'BB07', 'BO123BO', 20, 2),
(8, 'BB08', 'AA123AA', 32, 3),
(9, 'BB09', 'BB123BB', 32, 3);

-- --------------------------------------------------------

--
-- Structure de la table `lignes`
--

DROP TABLE IF EXISTS `lignes`;
CREATE TABLE `lignes` (
  `id_ligne` int(11) NOT NULL,
  `ligne` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `lignes`
--

INSERT INTO `lignes` (`id_ligne`, `ligne`) VALUES
(1, 'rouge'),
(2, 'vert'),
(3, 'bleu'),
(4, 'noir');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `arrets`
--
ALTER TABLE `arrets`
  ADD PRIMARY KEY (`id_arret`);

--
-- Index pour la table `arret_ligne`
--
ALTER TABLE `arret_ligne`
  ADD KEY `id_arret` (`id_arret`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Index pour la table `bus`
--
ALTER TABLE `bus`
  ADD PRIMARY KEY (`id_bus`),
  ADD KEY `id_ligne` (`id_ligne`);

--
-- Index pour la table `lignes`
--
ALTER TABLE `lignes`
  ADD PRIMARY KEY (`id_ligne`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `arrets`
--
ALTER TABLE `arrets`
  MODIFY `id_arret` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT pour la table `bus`
--
ALTER TABLE `bus`
  MODIFY `id_bus` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT pour la table `lignes`
--
ALTER TABLE `lignes`
  MODIFY `id_ligne` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `arret_ligne`
--
ALTER TABLE `arret_ligne`
  ADD CONSTRAINT `arret_ligne_ibfk_1` FOREIGN KEY (`id_arret`) REFERENCES `arrets` (`id_arret`),
  ADD CONSTRAINT `arret_ligne_ibfk_2` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);

--
-- Contraintes pour la table `bus`
--
ALTER TABLE `bus`
  ADD CONSTRAINT `bus_ibfk_1` FOREIGN KEY (`id_ligne`) REFERENCES `lignes` (`id_ligne`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
