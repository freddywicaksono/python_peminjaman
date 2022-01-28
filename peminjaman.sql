-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 28, 2022 at 02:12 PM
-- Server version: 10.4.14-MariaDB
-- PHP Version: 7.4.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `perpustakaan`
--

-- --------------------------------------------------------

--
-- Table structure for table `peminjaman`
--

CREATE TABLE `peminjaman` (
  `idpinjam` int(11) NOT NULL,
  `nomor_bukti` varchar(20) NOT NULL,
  `kode_anggota` varchar(20) NOT NULL,
  `tanggal_pinjam` date NOT NULL,
  `tanggal_haruskembali` date NOT NULL,
  `tanggal_kembali` date DEFAULT NULL,
  `kode_buku1` varchar(20) DEFAULT NULL,
  `kode_buku2` varchar(20) DEFAULT NULL,
  `kode_buku3` varchar(20) DEFAULT NULL,
  `sudah_dikembalikan` enum('Y','N') NOT NULL DEFAULT 'N'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `peminjaman`
--

INSERT INTO `peminjaman` (`idpinjam`, `nomor_bukti`, `kode_anggota`, `tanggal_pinjam`, `tanggal_haruskembali`, `tanggal_kembali`, `kode_buku1`, `kode_buku2`, `kode_buku3`, `sudah_dikembalikan`) VALUES
(1, '1122334455', '101', '2022-01-04', '2022-01-11', NULL, '2001', '2002', NULL, 'N'),
(2, '12345', '101', '2022-01-14', '2022-01-23', NULL, '2001', '', '', 'N'),
(4, '333', '102', '0000-00-00', '0000-00-00', NULL, '2001', '2002', '2003', 'N');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `peminjaman`
--
ALTER TABLE `peminjaman`
  ADD PRIMARY KEY (`idpinjam`),
  ADD UNIQUE KEY `unik` (`nomor_bukti`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `peminjaman`
--
ALTER TABLE `peminjaman`
  MODIFY `idpinjam` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
