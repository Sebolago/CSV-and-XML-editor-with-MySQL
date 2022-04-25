-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 20 Kwi 2022, 21:20
-- Wersja serwera: 10.4.21-MariaDB
-- Wersja PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `integracja`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `katalog`
--

CREATE TABLE `katalog` (
  `id` int(11) NOT NULL,
  `producent` varchar(50) NOT NULL,
  `przekatna` varchar(50) NOT NULL,
  `rozdzielczosc` varchar(50) NOT NULL,
  `matryca` varchar(50) NOT NULL,
  `dotykowy` varchar(50) NOT NULL,
  `procesor` varchar(50) NOT NULL,
  `rdzenie` varchar(50) NOT NULL,
  `taktowanie` varchar(50) NOT NULL,
  `RAM` varchar(50) NOT NULL,
  `dysk` varchar(50) NOT NULL,
  `typ dysku` varchar(50) NOT NULL,
  `grafika` varchar(50) NOT NULL,
  `VRAM` varchar(50) NOT NULL,
  `system` varchar(50) NOT NULL,
  `naped` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Zrzut danych tabeli `katalog`
--

INSERT INTO `katalog` (`id`, `producent`, `przekatna`, `rozdzielczosc`, `matryca`, `dotykowy`, `procesor`, `rdzenie`, `taktowanie`, `RAM`, `dysk`, `typ dysku`, `grafika`, `VRAM`, `system`, `naped`) VALUES
(1, 'Asus', '14\"', '1600x900', 'matowa', 'nie', 'intel i5', '4', '3000', '16GB', '256GB', 'SSD', 'Intel Iris', '1GB', 'Windows 10', 'brak'),
(2, 'Dell', '12\"', '', 'matowa', 'nie', 'intel i7', '4.0', '2800.0', '8GB', '240GB', 'SSD', 'intel HD Graphics 4000', '1GB', 'Windows 7 Home', ''),
(3, 'Asus', '14\"', '1600x900', 'matowa', 'nie', 'intel i5', '4.0', 'nan', '16GB', '120GB', 'SSD', 'intel HD Graphics 5000', '1GB', '', 'brak'),
(4, 'Fujitsu', '14\"', '1920x1080', 'blyszczaca', 'tak', 'intel i7', '8.0', '1900.0', '24GB', '500GB', 'HDD', 'intel HD Graphics 520', '1GB', 'brak systemu', 'Blu-Ray'),
(5, 'Huawei', '13\"', '', 'matowa', 'nie', 'intel i7', '4.0', '2400.0', '12GB', '24GB', 'HDD', 'NVIDIA GeForce GTX 1050', '', '', 'brak'),
(6, 'MSI', '17\"', '1600x900', 'blyszczaca', 'tak', 'intel i7', '4.0', '3300.0', '8GB', '60GB', 'SSD', 'AMD Radeon Pro 455', '1GB', 'Windows 8.1 Profesional', 'DVD'),
(7, 'Dell', '', '1280x800', 'matowa', 'nie', 'intel i7', '4.0', '2800.0', '8GB', '240GB', 'SSD', '', '', 'Windows 7 Home', 'brak'),
(8, 'Asus', '14\"', '1600x900', 'matowa', 'nie', 'intel i5', '4.0', '2800.0', '', '120GB', 'SSD', 'intel HD Graphics 5000', '1GB', 'Windows 10 Home', ''),
(9, 'Fujitsu', '15\"', '1920x1080', 'blyszczaca', 'tak', 'intel i7', '8.0', '2800.0', '24GB', '500GB', 'HDD', 'intel HD Graphics 520', '', 'brak systemu', 'Blu-Ray'),
(10, 'Samsung', '13\"', '1366x768', 'matowa', 'nie', 'intel i7', '4.0', '2800.0', '12GB', '24GB', 'HDD', 'NVIDIA GeForce GTX 1050', '1GB', 'Windows 10 Home', 'brak'),
(11, 'Sony', '16\"', '', 'blyszczaca', 'tak', 'intel i7', '4.0', '2800.0', '8GB', '', '', 'AMD Radeon Pro 455', '1GB', 'Windows 7 Profesional', 'DVD'),
(12, 'Samsung', '12\"', '1280x800', 'matowa', 'nie', 'intel i7', 'nan', '2120.0', '', '', '', 'intel HD Graphics 4000', '1GB', '', 'brak'),
(13, 'Samsung', '14\"', '1600x900', 'matowa', 'nie', 'intel i5', 'nan', 'nan', '', '', 'SSD', 'intel HD Graphics 5000', '1GB', 'Windows 10 Home', 'brak');

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `katalog`
--
ALTER TABLE `katalog`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `katalog`
--
ALTER TABLE `katalog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
