-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 04, 2022 at 11:12 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.0.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `accident_severity`
--

-- --------------------------------------------------------

--
-- Table structure for table `accidentdetails`
--

CREATE TABLE `accidentdetails` (
  `referencenumber` int(50) NOT NULL,
  `noofvehicles` varchar(50) NOT NULL,
  `roadtype` varchar(50) NOT NULL,
  `roadsurface` varchar(50) NOT NULL,
  `lightcondition` varchar(50) NOT NULL,
  `weather` varchar(50) NOT NULL,
  `casualityclass` varchar(50) NOT NULL,
  `casualitysex` varchar(50) NOT NULL,
  `casualityage` varchar(50) NOT NULL,
  `vehicletype` varchar(50) NOT NULL,
  `prediction` varchar(50) NOT NULL,
  `accidentdate` timestamp NOT NULL DEFAULT current_timestamp(),
  `user` varchar(50) NOT NULL,
  `place` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accidentdetails`
--

INSERT INTO `accidentdetails` (`referencenumber`, `noofvehicles`, `roadtype`, `roadsurface`, `lightcondition`, `weather`, `casualityclass`, `casualitysex`, `casualityage`, `vehicletype`, `prediction`, `accidentdate`, `user`, `place`) VALUES
(1, '21', '0', '0', '0', '0', '0', '0', '1', '0', '1', '2022-12-02 17:05:21', 'Prithiviraj', 'Che'),
(2, '1', '0', '0', '0', '0', '0', '0', '-1', '0', '0', '2022-12-02 17:21:44', '', 'Trt'),
(3, '2', '0', '1', '1', '8', '2', '0', '32', '3', '0', '2022-12-03 17:37:46', 'Prithiviraj', 'Chennai');

-- --------------------------------------------------------

--
-- Table structure for table `userdetails`
--

CREATE TABLE `userdetails` (
  `userid` int(10) NOT NULL,
  `username` varchar(255) NOT NULL,
  `role` varchar(255) NOT NULL,
  `phonennumber` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `purpose` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `createddata` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `userdetails`
--

INSERT INTO `userdetails` (`userid`, `username`, `role`, `phonennumber`, `email`, `purpose`, `password`, `createddata`) VALUES
(1, 'Prithiviraj', 'reporter', '6381268715', 'prithiv@gmail.com', 'Project', '121212', '2022-12-02 16:59:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accidentdetails`
--
ALTER TABLE `accidentdetails`
  ADD PRIMARY KEY (`referencenumber`);

--
-- Indexes for table `userdetails`
--
ALTER TABLE `userdetails`
  ADD PRIMARY KEY (`userid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accidentdetails`
--
ALTER TABLE `accidentdetails`
  MODIFY `referencenumber` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `userdetails`
--
ALTER TABLE `userdetails`
  MODIFY `userid` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
