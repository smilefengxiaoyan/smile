/*
 Navicat MySQL Data Transfer

 Source Server         : localhost_3306
 Source Server Type    : MySQL
 Source Server Version : 50721
 Source Host           : localhost:3306
 Source Schema         : personnel_man

 Target Server Type    : MySQL
 Target Server Version : 50721
 File Encoding         : 65001

 Date: 17/09/2018 12:05:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_table
-- ----------------------------
DROP TABLE IF EXISTS `admin_table`;
CREATE TABLE `admin_table`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pwd` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`s_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_table
-- ----------------------------
INSERT INTO `admin_table` VALUES ('000001', '1234');




-- ----------------------------
-- Table structure for staff
-- ----------------------------
DROP TABLE IF EXISTS `staff`;
CREATE TABLE `staff`  (
  `s_no` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_firstname` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_sex` char(2) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_birth` date NOT NULL,
  `s_email` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_company` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_quote` char(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_password` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`s_no`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `staff` VALUES ('000001', 'Schwarz','Lukas', 'M', '1987-09-10',  'wang@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000002', 'Schwarz','Lean', 'F', '1987-09-10',  'Leon@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000003', 'Müller','Lukas', 'M', '1987-09-10',  'wan@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000004', 'Grun','Lukas', 'M', '1987-09-10',  'wng@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000005', 'Black','Lukas', 'M', '1987-09-10',  'wag@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000006', 'Li','Lukas', 'M', '1987-09-10',  'lang@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000007', 'Schwarz','Jan', 'F', '1987-09-10',  'kang@163.com',  'BioTech','5', '1234');
INSERT INTO `staff` VALUES ('000008', 'Schwarz','Jan', 'F', '1987-09-10',  'kang@163.com',  'BioTech','5', '1234');




-- ----------------------------
-- Table structure for inva
-- ----------------------------
DROP TABLE IF EXISTS `inva`;
CREATE TABLE `inva`  (
  `s_vo` char(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_from` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_to` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_subject` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_message` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `s_name` char(8) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`s_vo`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of staff
-- ----------------------------
INSERT INTO `inva` VALUES ('000001', 'wang@163.com', 'Leon@163.com', 'thankyou',  'welcome ',  'maria');

SET FOREIGN_KEY_CHECKS = 1;














