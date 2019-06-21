/*
 Navicat Premium Data Transfer

 Source Server         : 47.98.63.111
 Source Server Type    : MySQL
 Source Server Version : 50644
 Source Host           : 47.98.63.111
 Source Database       : test

 Target Server Type    : MySQL
 Target Server Version : 50644
 File Encoding         : utf-8

 Date: 06/20/2019 22:45:37 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `category`
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `category`
-- ----------------------------
BEGIN;
INSERT INTO `category` VALUES ('1', '肉类'), ('2', '水果'), ('3', '蔬菜'), ('4', '日用');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
