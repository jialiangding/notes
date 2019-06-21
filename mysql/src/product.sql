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

 Date: 06/20/2019 22:46:00 PM
*/

SET NAMES utf8;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
--  Table structure for `product`
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category_id` int(11) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
--  Records of `product`
-- ----------------------------
BEGIN;
INSERT INTO `product` VALUES ('1', '1', '猪肉'), ('2', '1', '羊肉'), ('3', '1', '牛肉'), ('4', '2', '苹果'), ('5', '2', '香蕉'), ('6', '2', '橙子'), ('7', '3', '白菜'), ('8', '3', '卷心菜'), ('9', '3', '荷兰豆'), ('10', '5', '耳机');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
