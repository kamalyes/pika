/*
Navicat MySQL Data Transfer

Source Server         : 腾讯云
Source Server Version : 50735
Source Host           : host:3306
Source Database       : auto_test

Target Server Type    : MYSQL
Target Server Version : 50735
File Encoding         : 65001

Date: 2022-01-20 09:55:38
*/

SET
FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for administrative_area
-- ----------------------------
DROP TABLE IF EXISTS `administrative_area`;
CREATE TABLE `administrative_area`
(
    `id`             bigint(20) NOT NULL AUTO_INCREMENT,
    `area_code`      varchar(100)      DEFAULT NULL COMMENT '地区编码',
    `area_name`      varchar(100)      DEFAULT NULL COMMENT '地区名称',
    `area_level`     smallint(6) DEFAULT NULL COMMENT '地区等级: 1 省  2 市  3 区 4 区县 5 乡镇 6 村/社区',
    `parent_code`    varchar(100)      DEFAULT '' COMMENT '上级编码',
    `parent_id`      bigint(20) DEFAULT '0' COMMENT '上级ID',
    `status`         tinyint(1) DEFAULT '1' COMMENT '状态 0 禁用 1 启用',
    `create_time`    datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `update_time`    datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间',
    `create_user_no` bigint(20) DEFAULT '0' COMMENT '创建人',
    `update_user_no` bigint(20) DEFAULT '0' COMMENT '修改人',
    `active`         tinyint(1) DEFAULT '1' COMMENT '是否有效 0 否 1 是',
    PRIMARY KEY (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=3718 DEFAULT CHARSET=utf8mb4 COMMENT='地区';

-- ----------------------------
-- Records of administrative_area
-- ----------------------------
INSERT INTO `administrative_area`
VALUES ('1', '110000000000', '北京市', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2', '110100000000', '市辖区', '2', '110000000000', '1', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3', '110101000000', '东城区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('4', '110102000000', '西城区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('5', '110105000000', '朝阳区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('6', '110106000000', '丰台区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('7', '110107000000', '石景山区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('8', '110108000000', '海淀区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('9', '110109000000', '门头沟区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('10', '110111000000', '房山区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('11', '110112000000', '通州区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('12', '110113000000', '顺义区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('13', '110114000000', '昌平区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('14', '110115000000', '大兴区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('15', '110116000000', '怀柔区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('16', '110117000000', '平谷区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('17', '110118000000', '密云区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('18', '110119000000', '延庆区', '3', '110100000000', '2', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('19', '120000000000', '天津市', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('20', '120100000000', '市辖区', '2', '120000000000', '19', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('21', '120101000000', '和平区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('22', '120102000000', '河东区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('23', '120103000000', '河西区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('24', '120104000000', '南开区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('25', '120105000000', '河北区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('26', '120106000000', '红桥区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('27', '120110000000', '东丽区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('28', '120111000000', '西青区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('29', '120112000000', '津南区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('30', '120113000000', '北辰区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('31', '120114000000', '武清区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('32', '120115000000', '宝坻区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('33', '120116000000', '滨海新区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('34', '120117000000', '宁河区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('35', '120118000000', '静海区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('36', '120119000000', '蓟州区', '3', '120100000000', '20', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('37', '130000000000', '河北省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('38', '130100000000', '石家庄市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('39', '130101000000', '市辖区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('40', '130102000000', '长安区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('41', '130104000000', '桥西区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('42', '130105000000', '新华区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('43', '130107000000', '井陉矿区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('44', '130108000000', '裕华区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('45', '130109000000', '藁城区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('46', '130110000000', '鹿泉区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('47', '130111000000', '栾城区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('48', '130121000000', '井陉县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('49', '130123000000', '正定县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('50', '130125000000', '行唐县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('51', '130126000000', '灵寿县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('52', '130127000000', '高邑县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('53', '130128000000', '深泽县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('54', '130129000000', '赞皇县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('55', '130130000000', '无极县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('56', '130131000000', '平山县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('57', '130132000000', '元氏县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('58', '130133000000', '赵县', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('59', '130171000000', '石家庄高新技术产业开发区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('60', '130172000000', '石家庄循环化工园区', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('61', '130181000000', '辛集市', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('62', '130183000000', '晋州市', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('63', '130184000000', '新乐市', '3', '130100000000', '38', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('64', '130200000000', '唐山市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('65', '130201000000', '市辖区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('66', '130202000000', '路南区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('67', '130203000000', '路北区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('68', '130204000000', '古冶区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('69', '130205000000', '开平区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('70', '130207000000', '丰南区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('71', '130208000000', '丰润区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('72', '130209000000', '曹妃甸区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('73', '130224000000', '滦南县', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('74', '130225000000', '乐亭县', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('75', '130227000000', '迁西县', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('76', '130229000000', '玉田县', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('77', '130271000000', '河北唐山芦台经济开发区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('78', '130272000000', '唐山市汉沽管理区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('79', '130273000000', '唐山高新技术产业开发区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('80', '130274000000', '河北唐山海港经济开发区', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('81', '130281000000', '遵化市', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('82', '130283000000', '迁安市', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('83', '130284000000', '滦州市', '3', '130200000000', '64', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('84', '130300000000', '秦皇岛市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('85', '130301000000', '市辖区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('86', '130302000000', '海港区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('87', '130303000000', '山海关区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('88', '130304000000', '北戴河区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('89', '130306000000', '抚宁区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('90', '130321000000', '青龙满族自治县', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('91', '130322000000', '昌黎县', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('92', '130324000000', '卢龙县', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('93', '130371000000', '秦皇岛市经济技术开发区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('94', '130372000000', '北戴河新区', '3', '130300000000', '84', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('95', '130400000000', '邯郸市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('96', '130401000000', '市辖区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('97', '130402000000', '邯山区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('98', '130403000000', '丛台区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('99', '130404000000', '复兴区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('100', '130406000000', '峰峰矿区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('101', '130407000000', '肥乡区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('102', '130408000000', '永年区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('103', '130423000000', '临漳县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('104', '130424000000', '成安县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('105', '130425000000', '大名县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('106', '130426000000', '涉县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('107', '130427000000', '磁县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('108', '130430000000', '邱县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('109', '130431000000', '鸡泽县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('110', '130432000000', '广平县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('111', '130433000000', '馆陶县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('112', '130434000000', '魏县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('113', '130435000000', '曲周县', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('114', '130471000000', '邯郸经济技术开发区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('115', '130473000000', '邯郸冀南新区', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('116', '130481000000', '武安市', '3', '130400000000', '95', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('117', '130500000000', '邢台市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('118', '130501000000', '市辖区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('119', '130502000000', '襄都区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('120', '130503000000', '信都区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('121', '130505000000', '任泽区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('122', '130506000000', '南和区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('123', '130522000000', '临城县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('124', '130523000000', '内丘县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('125', '130524000000', '柏乡县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('126', '130525000000', '隆尧县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('127', '130528000000', '宁晋县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('128', '130529000000', '巨鹿县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('129', '130530000000', '新河县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('130', '130531000000', '广宗县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('131', '130532000000', '平乡县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('132', '130533000000', '威县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('133', '130534000000', '清河县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('134', '130535000000', '临西县', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('135', '130571000000', '河北邢台经济开发区', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('136', '130581000000', '南宫市', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('137', '130582000000', '沙河市', '3', '130500000000', '117', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('138', '130600000000', '保定市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('139', '130601000000', '市辖区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('140', '130602000000', '竞秀区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('141', '130606000000', '莲池区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('142', '130607000000', '满城区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('143', '130608000000', '清苑区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('144', '130609000000', '徐水区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('145', '130623000000', '涞水县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('146', '130624000000', '阜平县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('147', '130626000000', '定兴县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('148', '130627000000', '唐县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('149', '130628000000', '高阳县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('150', '130629000000', '容城县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('151', '130630000000', '涞源县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('152', '130631000000', '望都县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('153', '130632000000', '安新县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('154', '130633000000', '易县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('155', '130634000000', '曲阳县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('156', '130635000000', '蠡县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('157', '130636000000', '顺平县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('158', '130637000000', '博野县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('159', '130638000000', '雄县', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('160', '130671000000', '保定高新技术产业开发区', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('161', '130672000000', '保定白沟新城', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('162', '130681000000', '涿州市', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('163', '130682000000', '定州市', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('164', '130683000000', '安国市', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('165', '130684000000', '高碑店市', '3', '130600000000', '138', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('166', '130700000000', '张家口市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('167', '130701000000', '市辖区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('168', '130702000000', '桥东区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('169', '130703000000', '桥西区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('170', '130705000000', '宣化区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('171', '130706000000', '下花园区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('172', '130708000000', '万全区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('173', '130709000000', '崇礼区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('174', '130722000000', '张北县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('175', '130723000000', '康保县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('176', '130724000000', '沽源县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('177', '130725000000', '尚义县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('178', '130726000000', '蔚县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('179', '130727000000', '阳原县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('180', '130728000000', '怀安县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('181', '130730000000', '怀来县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('182', '130731000000', '涿鹿县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('183', '130732000000', '赤城县', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('184', '130771000000', '张家口经济开发区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('185', '130772000000', '张家口市察北管理区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('186', '130773000000', '张家口市塞北管理区', '3', '130700000000', '166', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('187', '130800000000', '承德市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('188', '130801000000', '市辖区', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('189', '130802000000', '双桥区', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('190', '130803000000', '双滦区', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('191', '130804000000', '鹰手营子矿区', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('192', '130821000000', '承德县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('193', '130822000000', '兴隆县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('194', '130824000000', '滦平县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('195', '130825000000', '隆化县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('196', '130826000000', '丰宁满族自治县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('197', '130827000000', '宽城满族自治县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('198', '130828000000', '围场满族蒙古族自治县', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('199', '130871000000', '承德高新技术产业开发区', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('200', '130881000000', '平泉市', '3', '130800000000', '187', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('201', '130900000000', '沧州市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('202', '130901000000', '市辖区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('203', '130902000000', '新华区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('204', '130903000000', '运河区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('205', '130921000000', '沧县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('206', '130922000000', '青县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('207', '130923000000', '东光县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('208', '130924000000', '海兴县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('209', '130925000000', '盐山县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('210', '130926000000', '肃宁县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('211', '130927000000', '南皮县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('212', '130928000000', '吴桥县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('213', '130929000000', '献县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('214', '130930000000', '孟村回族自治县', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('215', '130971000000', '河北沧州经济开发区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('216', '130972000000', '沧州高新技术产业开发区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('217', '130973000000', '沧州渤海新区', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('218', '130981000000', '泊头市', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('219', '130982000000', '任丘市', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('220', '130983000000', '黄骅市', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('221', '130984000000', '河间市', '3', '130900000000', '201', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('222', '131000000000', '廊坊市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('223', '131001000000', '市辖区', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('224', '131002000000', '安次区', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('225', '131003000000', '广阳区', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('226', '131022000000', '固安县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('227', '131023000000', '永清县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('228', '131024000000', '香河县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('229', '131025000000', '大城县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('230', '131026000000', '文安县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('231', '131028000000', '大厂回族自治县', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('232', '131071000000', '廊坊经济技术开发区', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('233', '131081000000', '霸州市', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('234', '131082000000', '三河市', '3', '131000000000', '222', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('235', '131100000000', '衡水市', '2', '130000000000', '37', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('236', '131101000000', '市辖区', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('237', '131102000000', '桃城区', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('238', '131103000000', '冀州区', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('239', '131121000000', '枣强县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('240', '131122000000', '武邑县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('241', '131123000000', '武强县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('242', '131124000000', '饶阳县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('243', '131125000000', '安平县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('244', '131126000000', '故城县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('245', '131127000000', '景县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('246', '131128000000', '阜城县', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('247', '131171000000', '河北衡水高新技术产业开发区', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('248', '131172000000', '衡水滨湖新区', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('249', '131182000000', '深州市', '3', '131100000000', '235', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('250', '140000000000', '山西省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('251', '140100000000', '太原市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('252', '140101000000', '市辖区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('253', '140105000000', '小店区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('254', '140106000000', '迎泽区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('255', '140107000000', '杏花岭区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('256', '140108000000', '尖草坪区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('257', '140109000000', '万柏林区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('258', '140110000000', '晋源区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('259', '140121000000', '清徐县', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('260', '140122000000', '阳曲县', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('261', '140123000000', '娄烦县', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('262', '140171000000', '山西转型综合改革示范区', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('263', '140181000000', '古交市', '3', '140100000000', '251', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('264', '140200000000', '大同市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('265', '140201000000', '市辖区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('266', '140212000000', '新荣区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('267', '140213000000', '平城区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('268', '140214000000', '云冈区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('269', '140215000000', '云州区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('270', '140221000000', '阳高县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('271', '140222000000', '天镇县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('272', '140223000000', '广灵县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('273', '140224000000', '灵丘县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('274', '140225000000', '浑源县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('275', '140226000000', '左云县', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('276', '140271000000', '山西大同经济开发区', '3', '140200000000', '264', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('277', '140300000000', '阳泉市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('278', '140301000000', '市辖区', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('279', '140302000000', '城区', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('280', '140303000000', '矿区', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('281', '140311000000', '郊区', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('282', '140321000000', '平定县', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('283', '140322000000', '盂县', '3', '140300000000', '277', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('284', '140400000000', '长治市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('285', '140401000000', '市辖区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('286', '140403000000', '潞州区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('287', '140404000000', '上党区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('288', '140405000000', '屯留区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('289', '140406000000', '潞城区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('290', '140423000000', '襄垣县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('291', '140425000000', '平顺县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('292', '140426000000', '黎城县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('293', '140427000000', '壶关县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('294', '140428000000', '长子县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('295', '140429000000', '武乡县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('296', '140430000000', '沁县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('297', '140431000000', '沁源县', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('298', '140471000000', '山西长治高新技术产业园区', '3', '140400000000', '284', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('299', '140500000000', '晋城市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('300', '140501000000', '市辖区', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('301', '140502000000', '城区', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('302', '140521000000', '沁水县', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('303', '140522000000', '阳城县', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('304', '140524000000', '陵川县', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('305', '140525000000', '泽州县', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('306', '140581000000', '高平市', '3', '140500000000', '299', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('307', '140600000000', '朔州市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('308', '140601000000', '市辖区', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('309', '140602000000', '朔城区', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('310', '140603000000', '平鲁区', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('311', '140621000000', '山阴县', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('312', '140622000000', '应县', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('313', '140623000000', '右玉县', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('314', '140671000000', '山西朔州经济开发区', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('315', '140681000000', '怀仁市', '3', '140600000000', '307', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('316', '140700000000', '晋中市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('317', '140701000000', '市辖区', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('318', '140702000000', '榆次区', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('319', '140703000000', '太谷区', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('320', '140721000000', '榆社县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('321', '140722000000', '左权县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('322', '140723000000', '和顺县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('323', '140724000000', '昔阳县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('324', '140725000000', '寿阳县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('325', '140727000000', '祁县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('326', '140728000000', '平遥县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('327', '140729000000', '灵石县', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('328', '140781000000', '介休市', '3', '140700000000', '316', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('329', '140800000000', '运城市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('330', '140801000000', '市辖区', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('331', '140802000000', '盐湖区', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('332', '140821000000', '临猗县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('333', '140822000000', '万荣县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('334', '140823000000', '闻喜县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('335', '140824000000', '稷山县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('336', '140825000000', '新绛县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('337', '140826000000', '绛县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('338', '140827000000', '垣曲县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('339', '140828000000', '夏县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('340', '140829000000', '平陆县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('341', '140830000000', '芮城县', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('342', '140881000000', '永济市', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('343', '140882000000', '河津市', '3', '140800000000', '329', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('344', '140900000000', '忻州市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('345', '140901000000', '市辖区', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('346', '140902000000', '忻府区', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('347', '140921000000', '定襄县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('348', '140922000000', '五台县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('349', '140923000000', '代县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('350', '140924000000', '繁峙县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('351', '140925000000', '宁武县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('352', '140926000000', '静乐县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('353', '140927000000', '神池县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('354', '140928000000', '五寨县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('355', '140929000000', '岢岚县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('356', '140930000000', '河曲县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('357', '140931000000', '保德县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('358', '140932000000', '偏关县', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('359', '140971000000', '五台山风景名胜区', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('360', '140981000000', '原平市', '3', '140900000000', '344', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('361', '141000000000', '临汾市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('362', '141001000000', '市辖区', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('363', '141002000000', '尧都区', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('364', '141021000000', '曲沃县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('365', '141022000000', '翼城县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('366', '141023000000', '襄汾县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('367', '141024000000', '洪洞县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('368', '141025000000', '古县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('369', '141026000000', '安泽县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('370', '141027000000', '浮山县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('371', '141028000000', '吉县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('372', '141029000000', '乡宁县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('373', '141030000000', '大宁县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('374', '141031000000', '隰县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('375', '141032000000', '永和县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('376', '141033000000', '蒲县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('377', '141034000000', '汾西县', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('378', '141081000000', '侯马市', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('379', '141082000000', '霍州市', '3', '141000000000', '361', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('380', '141100000000', '吕梁市', '2', '140000000000', '250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('381', '141101000000', '市辖区', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('382', '141102000000', '离石区', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('383', '141121000000', '文水县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('384', '141122000000', '交城县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('385', '141123000000', '兴县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('386', '141124000000', '临县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('387', '141125000000', '柳林县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('388', '141126000000', '石楼县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('389', '141127000000', '岚县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('390', '141128000000', '方山县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('391', '141129000000', '中阳县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('392', '141130000000', '交口县', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('393', '141181000000', '孝义市', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('394', '141182000000', '汾阳市', '3', '141100000000', '380', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('395', '150000000000', '内蒙古自治区', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('396', '150100000000', '呼和浩特市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('397', '150101000000', '市辖区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('398', '150102000000', '新城区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('399', '150103000000', '回民区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('400', '150104000000', '玉泉区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('401', '150105000000', '赛罕区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('402', '150121000000', '土默特左旗', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('403', '150122000000', '托克托县', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('404', '150123000000', '和林格尔县', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('405', '150124000000', '清水河县', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('406', '150125000000', '武川县', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('407', '150172000000', '呼和浩特经济技术开发区', '3', '150100000000', '396', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('408', '150200000000', '包头市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('409', '150201000000', '市辖区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('410', '150202000000', '东河区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('411', '150203000000', '昆都仑区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('412', '150204000000', '青山区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('413', '150205000000', '石拐区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('414', '150206000000', '白云鄂博矿区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('415', '150207000000', '九原区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('416', '150221000000', '土默特右旗', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('417', '150222000000', '固阳县', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('418', '150223000000', '达尔罕茂明安联合旗', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('419', '150271000000', '包头稀土高新技术产业开发区', '3', '150200000000', '408', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('420', '150300000000', '乌海市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('421', '150301000000', '市辖区', '3', '150300000000', '420', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('422', '150302000000', '海勃湾区', '3', '150300000000', '420', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('423', '150303000000', '海南区', '3', '150300000000', '420', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('424', '150304000000', '乌达区', '3', '150300000000', '420', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('425', '150400000000', '赤峰市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('426', '150401000000', '市辖区', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('427', '150402000000', '红山区', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('428', '150403000000', '元宝山区', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('429', '150404000000', '松山区', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('430', '150421000000', '阿鲁科尔沁旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('431', '150422000000', '巴林左旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('432', '150423000000', '巴林右旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('433', '150424000000', '林西县', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('434', '150425000000', '克什克腾旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('435', '150426000000', '翁牛特旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('436', '150428000000', '喀喇沁旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('437', '150429000000', '宁城县', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('438', '150430000000', '敖汉旗', '3', '150400000000', '425', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('439', '150500000000', '通辽市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('440', '150501000000', '市辖区', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('441', '150502000000', '科尔沁区', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('442', '150521000000', '科尔沁左翼中旗', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('443', '150522000000', '科尔沁左翼后旗', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('444', '150523000000', '开鲁县', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('445', '150524000000', '库伦旗', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('446', '150525000000', '奈曼旗', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('447', '150526000000', '扎鲁特旗', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('448', '150571000000', '通辽经济技术开发区', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('449', '150581000000', '霍林郭勒市', '3', '150500000000', '439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('450', '150600000000', '鄂尔多斯市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('451', '150601000000', '市辖区', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('452', '150602000000', '东胜区', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('453', '150603000000', '康巴什区', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('454', '150621000000', '达拉特旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('455', '150622000000', '准格尔旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('456', '150623000000', '鄂托克前旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('457', '150624000000', '鄂托克旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('458', '150625000000', '杭锦旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('459', '150626000000', '乌审旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('460', '150627000000', '伊金霍洛旗', '3', '150600000000', '450', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('461', '150700000000', '呼伦贝尔市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('462', '150701000000', '市辖区', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('463', '150702000000', '海拉尔区', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('464', '150703000000', '扎赉诺尔区', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('465', '150721000000', '阿荣旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('466', '150722000000', '莫力达瓦达斡尔族自治旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('467', '150723000000', '鄂伦春自治旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('468', '150724000000', '鄂温克族自治旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('469', '150725000000', '陈巴尔虎旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('470', '150726000000', '新巴尔虎左旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('471', '150727000000', '新巴尔虎右旗', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('472', '150781000000', '满洲里市', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('473', '150782000000', '牙克石市', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('474', '150783000000', '扎兰屯市', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('475', '150784000000', '额尔古纳市', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('476', '150785000000', '根河市', '3', '150700000000', '461', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('477', '150800000000', '巴彦淖尔市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('478', '150801000000', '市辖区', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('479', '150802000000', '临河区', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('480', '150821000000', '五原县', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('481', '150822000000', '磴口县', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('482', '150823000000', '乌拉特前旗', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('483', '150824000000', '乌拉特中旗', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('484', '150825000000', '乌拉特后旗', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('485', '150826000000', '杭锦后旗', '3', '150800000000', '477', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('486', '150900000000', '乌兰察布市', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('487', '150901000000', '市辖区', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('488', '150902000000', '集宁区', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('489', '150921000000', '卓资县', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('490', '150922000000', '化德县', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('491', '150923000000', '商都县', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('492', '150924000000', '兴和县', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('493', '150925000000', '凉城县', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('494', '150926000000', '察哈尔右翼前旗', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('495', '150927000000', '察哈尔右翼中旗', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('496', '150928000000', '察哈尔右翼后旗', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('497', '150929000000', '四子王旗', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('498', '150981000000', '丰镇市', '3', '150900000000', '486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('499', '152200000000', '兴安盟', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('500', '152201000000', '乌兰浩特市', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('501', '152202000000', '阿尔山市', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('502', '152221000000', '科尔沁右翼前旗', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('503', '152222000000', '科尔沁右翼中旗', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('504', '152223000000', '扎赉特旗', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('505', '152224000000', '突泉县', '3', '152200000000', '499', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('506', '152500000000', '锡林郭勒盟', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('507', '152501000000', '二连浩特市', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('508', '152502000000', '锡林浩特市', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('509', '152522000000', '阿巴嘎旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('510', '152523000000', '苏尼特左旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('511', '152524000000', '苏尼特右旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('512', '152525000000', '东乌珠穆沁旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('513', '152526000000', '西乌珠穆沁旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('514', '152527000000', '太仆寺旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('515', '152528000000', '镶黄旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('516', '152529000000', '正镶白旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('517', '152530000000', '正蓝旗', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('518', '152531000000', '多伦县', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('519', '152571000000', '乌拉盖管委会', '3', '152500000000', '506', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('520', '152900000000', '阿拉善盟', '2', '150000000000', '395', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('521', '152921000000', '阿拉善左旗', '3', '152900000000', '520', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('522', '152922000000', '阿拉善右旗', '3', '152900000000', '520', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('523', '152923000000', '额济纳旗', '3', '152900000000', '520', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('524', '152971000000', '内蒙古阿拉善高新技术产业开发区', '3', '152900000000', '520', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('525', '210000000000', '辽宁省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('526', '210100000000', '沈阳市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('527', '210101000000', '市辖区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('528', '210102000000', '和平区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('529', '210103000000', '沈河区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('530', '210104000000', '大东区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('531', '210105000000', '皇姑区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('532', '210106000000', '铁西区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('533', '210111000000', '苏家屯区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('534', '210112000000', '浑南区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('535', '210113000000', '沈北新区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('536', '210114000000', '于洪区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('537', '210115000000', '辽中区', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('538', '210123000000', '康平县', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('539', '210124000000', '法库县', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('540', '210181000000', '新民市', '3', '210100000000', '526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('541', '210200000000', '大连市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('542', '210201000000', '市辖区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('543', '210202000000', '中山区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('544', '210203000000', '西岗区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('545', '210204000000', '沙河口区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('546', '210211000000', '甘井子区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('547', '210212000000', '旅顺口区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('548', '210213000000', '金州区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('549', '210214000000', '普兰店区', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('550', '210224000000', '长海县', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('551', '210281000000', '瓦房店市', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('552', '210283000000', '庄河市', '3', '210200000000', '541', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('553', '210300000000', '鞍山市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('554', '210301000000', '市辖区', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('555', '210302000000', '铁东区', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('556', '210303000000', '铁西区', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('557', '210304000000', '立山区', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('558', '210311000000', '千山区', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('559', '210321000000', '台安县', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('560', '210323000000', '岫岩满族自治县', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('561', '210381000000', '海城市', '3', '210300000000', '553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('562', '210400000000', '抚顺市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('563', '210401000000', '市辖区', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('564', '210402000000', '新抚区', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('565', '210403000000', '东洲区', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('566', '210404000000', '望花区', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('567', '210411000000', '顺城区', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('568', '210421000000', '抚顺县', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('569', '210422000000', '新宾满族自治县', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('570', '210423000000', '清原满族自治县', '3', '210400000000', '562', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('571', '210500000000', '本溪市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('572', '210501000000', '市辖区', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('573', '210502000000', '平山区', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('574', '210503000000', '溪湖区', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('575', '210504000000', '明山区', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('576', '210505000000', '南芬区', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('577', '210521000000', '本溪满族自治县', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('578', '210522000000', '桓仁满族自治县', '3', '210500000000', '571', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('579', '210600000000', '丹东市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('580', '210601000000', '市辖区', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('581', '210602000000', '元宝区', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('582', '210603000000', '振兴区', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('583', '210604000000', '振安区', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('584', '210624000000', '宽甸满族自治县', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('585', '210681000000', '东港市', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('586', '210682000000', '凤城市', '3', '210600000000', '579', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('587', '210700000000', '锦州市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('588', '210701000000', '市辖区', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('589', '210702000000', '古塔区', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('590', '210703000000', '凌河区', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('591', '210711000000', '太和区', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('592', '210726000000', '黑山县', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('593', '210727000000', '义县', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('594', '210781000000', '凌海市', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('595', '210782000000', '北镇市', '3', '210700000000', '587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('596', '210800000000', '营口市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('597', '210801000000', '市辖区', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('598', '210802000000', '站前区', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('599', '210803000000', '西市区', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('600', '210804000000', '鲅鱼圈区', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('601', '210811000000', '老边区', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('602', '210881000000', '盖州市', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('603', '210882000000', '大石桥市', '3', '210800000000', '596', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('604', '210900000000', '阜新市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('605', '210901000000', '市辖区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('606', '210902000000', '海州区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('607', '210903000000', '新邱区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('608', '210904000000', '太平区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('609', '210905000000', '清河门区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('610', '210911000000', '细河区', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('611', '210921000000', '阜新蒙古族自治县', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('612', '210922000000', '彰武县', '3', '210900000000', '604', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('613', '211000000000', '辽阳市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('614', '211001000000', '市辖区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('615', '211002000000', '白塔区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('616', '211003000000', '文圣区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('617', '211004000000', '宏伟区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('618', '211005000000', '弓长岭区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('619', '211011000000', '太子河区', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('620', '211021000000', '辽阳县', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('621', '211081000000', '灯塔市', '3', '211000000000', '613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('622', '211100000000', '盘锦市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('623', '211101000000', '市辖区', '3', '211100000000', '622', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('624', '211102000000', '双台子区', '3', '211100000000', '622', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('625', '211103000000', '兴隆台区', '3', '211100000000', '622', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('626', '211104000000', '大洼区', '3', '211100000000', '622', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('627', '211122000000', '盘山县', '3', '211100000000', '622', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('628', '211200000000', '铁岭市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('629', '211201000000', '市辖区', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('630', '211202000000', '银州区', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('631', '211204000000', '清河区', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('632', '211221000000', '铁岭县', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('633', '211223000000', '西丰县', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('634', '211224000000', '昌图县', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('635', '211281000000', '调兵山市', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('636', '211282000000', '开原市', '3', '211200000000', '628', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('637', '211300000000', '朝阳市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('638', '211301000000', '市辖区', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('639', '211302000000', '双塔区', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('640', '211303000000', '龙城区', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('641', '211321000000', '朝阳县', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('642', '211322000000', '建平县', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('643', '211324000000', '喀喇沁左翼蒙古族自治县', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('644', '211381000000', '北票市', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('645', '211382000000', '凌源市', '3', '211300000000', '637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('646', '211400000000', '葫芦岛市', '2', '210000000000', '525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('647', '211401000000', '市辖区', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('648', '211402000000', '连山区', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('649', '211403000000', '龙港区', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('650', '211404000000', '南票区', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('651', '211421000000', '绥中县', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('652', '211422000000', '建昌县', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('653', '211481000000', '兴城市', '3', '211400000000', '646', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('654', '220000000000', '吉林省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('655', '220100000000', '长春市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('656', '220101000000', '市辖区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('657', '220102000000', '南关区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('658', '220103000000', '宽城区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('659', '220104000000', '朝阳区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('660', '220105000000', '二道区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('661', '220106000000', '绿园区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('662', '220112000000', '双阳区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('663', '220113000000', '九台区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('664', '220122000000', '农安县', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('665', '220171000000', '长春经济技术开发区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('666', '220172000000', '长春净月高新技术产业开发区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('667', '220173000000', '长春高新技术产业开发区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('668', '220174000000', '长春汽车经济技术开发区', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('669', '220182000000', '榆树市', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('670', '220183000000', '德惠市', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('671', '220184000000', '公主岭市', '3', '220100000000', '655', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('672', '220200000000', '吉林市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('673', '220201000000', '市辖区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('674', '220202000000', '昌邑区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('675', '220203000000', '龙潭区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('676', '220204000000', '船营区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('677', '220211000000', '丰满区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('678', '220221000000', '永吉县', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('679', '220271000000', '吉林经济开发区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('680', '220272000000', '吉林高新技术产业开发区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('681', '220273000000', '吉林中国新加坡食品区', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('682', '220281000000', '蛟河市', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('683', '220282000000', '桦甸市', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('684', '220283000000', '舒兰市', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('685', '220284000000', '磐石市', '3', '220200000000', '672', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('686', '220300000000', '四平市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('687', '220301000000', '市辖区', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('688', '220302000000', '铁西区', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('689', '220303000000', '铁东区', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('690', '220322000000', '梨树县', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('691', '220323000000', '伊通满族自治县', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('692', '220382000000', '双辽市', '3', '220300000000', '686', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('693', '220400000000', '辽源市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('694', '220401000000', '市辖区', '3', '220400000000', '693', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('695', '220402000000', '龙山区', '3', '220400000000', '693', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('696', '220403000000', '西安区', '3', '220400000000', '693', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('697', '220421000000', '东丰县', '3', '220400000000', '693', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('698', '220422000000', '东辽县', '3', '220400000000', '693', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('699', '220500000000', '通化市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('700', '220501000000', '市辖区', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('701', '220502000000', '东昌区', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('702', '220503000000', '二道江区', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('703', '220521000000', '通化县', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('704', '220523000000', '辉南县', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('705', '220524000000', '柳河县', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('706', '220581000000', '梅河口市', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('707', '220582000000', '集安市', '3', '220500000000', '699', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('708', '220600000000', '白山市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('709', '220601000000', '市辖区', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('710', '220602000000', '浑江区', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('711', '220605000000', '江源区', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('712', '220621000000', '抚松县', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('713', '220622000000', '靖宇县', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('714', '220623000000', '长白朝鲜族自治县', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('715', '220681000000', '临江市', '3', '220600000000', '708', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('716', '220700000000', '松原市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('717', '220701000000', '市辖区', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('718', '220702000000', '宁江区', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('719', '220721000000', '前郭尔罗斯蒙古族自治县', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('720', '220722000000', '长岭县', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('721', '220723000000', '乾安县', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('722', '220771000000', '吉林松原经济开发区', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('723', '220781000000', '扶余市', '3', '220700000000', '716', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('724', '220800000000', '白城市', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('725', '220801000000', '市辖区', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('726', '220802000000', '洮北区', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('727', '220821000000', '镇赉县', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('728', '220822000000', '通榆县', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('729', '220871000000', '吉林白城经济开发区', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('730', '220881000000', '洮南市', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('731', '220882000000', '大安市', '3', '220800000000', '724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('732', '222400000000', '延边朝鲜族自治州', '2', '220000000000', '654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('733', '222401000000', '延吉市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('734', '222402000000', '图们市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('735', '222403000000', '敦化市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('736', '222404000000', '珲春市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('737', '222405000000', '龙井市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('738', '222406000000', '和龙市', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('739', '222424000000', '汪清县', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('740', '222426000000', '安图县', '3', '222400000000', '732', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('741', '230000000000', '黑龙江省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('742', '230100000000', '哈尔滨市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('743', '230101000000', '市辖区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('744', '230102000000', '道里区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('745', '230103000000', '南岗区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('746', '230104000000', '道外区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('747', '230108000000', '平房区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('748', '230109000000', '松北区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('749', '230110000000', '香坊区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('750', '230111000000', '呼兰区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('751', '230112000000', '阿城区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('752', '230113000000', '双城区', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('753', '230123000000', '依兰县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('754', '230124000000', '方正县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('755', '230125000000', '宾县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('756', '230126000000', '巴彦县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('757', '230127000000', '木兰县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('758', '230128000000', '通河县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('759', '230129000000', '延寿县', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('760', '230183000000', '尚志市', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('761', '230184000000', '五常市', '3', '230100000000', '742', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('762', '230200000000', '齐齐哈尔市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('763', '230201000000', '市辖区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('764', '230202000000', '龙沙区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('765', '230203000000', '建华区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('766', '230204000000', '铁锋区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('767', '230205000000', '昂昂溪区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('768', '230206000000', '富拉尔基区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('769', '230207000000', '碾子山区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('770', '230208000000', '梅里斯达斡尔族区', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('771', '230221000000', '龙江县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('772', '230223000000', '依安县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('773', '230224000000', '泰来县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('774', '230225000000', '甘南县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('775', '230227000000', '富裕县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('776', '230229000000', '克山县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('777', '230230000000', '克东县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('778', '230231000000', '拜泉县', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('779', '230281000000', '讷河市', '3', '230200000000', '762', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('780', '230300000000', '鸡西市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('781', '230301000000', '市辖区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('782', '230302000000', '鸡冠区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('783', '230303000000', '恒山区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('784', '230304000000', '滴道区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('785', '230305000000', '梨树区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('786', '230306000000', '城子河区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('787', '230307000000', '麻山区', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('788', '230321000000', '鸡东县', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('789', '230381000000', '虎林市', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('790', '230382000000', '密山市', '3', '230300000000', '780', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('791', '230400000000', '鹤岗市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('792', '230401000000', '市辖区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('793', '230402000000', '向阳区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('794', '230403000000', '工农区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('795', '230404000000', '南山区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('796', '230405000000', '兴安区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('797', '230406000000', '东山区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('798', '230407000000', '兴山区', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('799', '230421000000', '萝北县', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('800', '230422000000', '绥滨县', '3', '230400000000', '791', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('801', '230500000000', '双鸭山市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('802', '230501000000', '市辖区', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('803', '230502000000', '尖山区', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('804', '230503000000', '岭东区', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('805', '230505000000', '四方台区', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('806', '230506000000', '宝山区', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('807', '230521000000', '集贤县', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('808', '230522000000', '友谊县', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('809', '230523000000', '宝清县', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('810', '230524000000', '饶河县', '3', '230500000000', '801', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('811', '230600000000', '大庆市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('812', '230601000000', '市辖区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('813', '230602000000', '萨尔图区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('814', '230603000000', '龙凤区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('815', '230604000000', '让胡路区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('816', '230605000000', '红岗区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('817', '230606000000', '大同区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('818', '230621000000', '肇州县', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('819', '230622000000', '肇源县', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('820', '230623000000', '林甸县', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('821', '230624000000', '杜尔伯特蒙古族自治县', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('822', '230671000000', '大庆高新技术产业开发区', '3', '230600000000', '811', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('823', '230700000000', '伊春市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('824', '230701000000', '市辖区', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('825', '230717000000', '伊美区', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('826', '230718000000', '乌翠区', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('827', '230719000000', '友好区', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('828', '230722000000', '嘉荫县', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('829', '230723000000', '汤旺县', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('830', '230724000000', '丰林县', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('831', '230725000000', '大箐山县', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('832', '230726000000', '南岔县', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('833', '230751000000', '金林区', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('834', '230781000000', '铁力市', '3', '230700000000', '823', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('835', '230800000000', '佳木斯市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('836', '230801000000', '市辖区', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('837', '230803000000', '向阳区', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('838', '230804000000', '前进区', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('839', '230805000000', '东风区', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('840', '230811000000', '郊区', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('841', '230822000000', '桦南县', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('842', '230826000000', '桦川县', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('843', '230828000000', '汤原县', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('844', '230881000000', '同江市', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('845', '230882000000', '富锦市', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('846', '230883000000', '抚远市', '3', '230800000000', '835', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('847', '230900000000', '七台河市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('848', '230901000000', '市辖区', '3', '230900000000', '847', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('849', '230902000000', '新兴区', '3', '230900000000', '847', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('850', '230903000000', '桃山区', '3', '230900000000', '847', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('851', '230904000000', '茄子河区', '3', '230900000000', '847', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('852', '230921000000', '勃利县', '3', '230900000000', '847', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('853', '231000000000', '牡丹江市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('854', '231001000000', '市辖区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('855', '231002000000', '东安区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('856', '231003000000', '阳明区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('857', '231004000000', '爱民区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('858', '231005000000', '西安区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('859', '231025000000', '林口县', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('860', '231071000000', '牡丹江经济技术开发区', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('861', '231081000000', '绥芬河市', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('862', '231083000000', '海林市', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('863', '231084000000', '宁安市', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('864', '231085000000', '穆棱市', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('865', '231086000000', '东宁市', '3', '231000000000', '853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('866', '231100000000', '黑河市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('867', '231101000000', '市辖区', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('868', '231102000000', '爱辉区', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('869', '231123000000', '逊克县', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('870', '231124000000', '孙吴县', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('871', '231181000000', '北安市', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('872', '231182000000', '五大连池市', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('873', '231183000000', '嫩江市', '3', '231100000000', '866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('874', '231200000000', '绥化市', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('875', '231201000000', '市辖区', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('876', '231202000000', '北林区', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('877', '231221000000', '望奎县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('878', '231222000000', '兰西县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('879', '231223000000', '青冈县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('880', '231224000000', '庆安县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('881', '231225000000', '明水县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('882', '231226000000', '绥棱县', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('883', '231281000000', '安达市', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('884', '231282000000', '肇东市', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('885', '231283000000', '海伦市', '3', '231200000000', '874', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('886', '232700000000', '大兴安岭地区', '2', '230000000000', '741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('887', '232701000000', '漠河市', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('888', '232721000000', '呼玛县', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('889', '232722000000', '塔河县', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('890', '232761000000', '加格达奇区', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('891', '232762000000', '松岭区', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('892', '232763000000', '新林区', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('893', '232764000000', '呼中区', '3', '232700000000', '886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('894', '310000000000', '上海市', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('895', '310100000000', '市辖区', '2', '310000000000', '894', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('896', '310101000000', '黄浦区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('897', '310104000000', '徐汇区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('898', '310105000000', '长宁区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('899', '310106000000', '静安区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('900', '310107000000', '普陀区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('901', '310109000000', '虹口区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('902', '310110000000', '杨浦区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('903', '310112000000', '闵行区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('904', '310113000000', '宝山区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('905', '310114000000', '嘉定区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('906', '310115000000', '浦东新区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('907', '310116000000', '金山区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('908', '310117000000', '松江区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('909', '310118000000', '青浦区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('910', '310120000000', '奉贤区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('911', '310151000000', '崇明区', '3', '310100000000', '895', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('912', '320000000000', '江苏省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('913', '320100000000', '南京市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('914', '320101000000', '市辖区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('915', '320102000000', '玄武区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('916', '320104000000', '秦淮区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('917', '320105000000', '建邺区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('918', '320106000000', '鼓楼区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('919', '320111000000', '浦口区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('920', '320113000000', '栖霞区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('921', '320114000000', '雨花台区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('922', '320115000000', '江宁区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('923', '320116000000', '六合区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('924', '320117000000', '溧水区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('925', '320118000000', '高淳区', '3', '320100000000', '913', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('926', '320200000000', '无锡市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('927', '320201000000', '市辖区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('928', '320205000000', '锡山区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('929', '320206000000', '惠山区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('930', '320211000000', '滨湖区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('931', '320213000000', '梁溪区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('932', '320214000000', '新吴区', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('933', '320281000000', '江阴市', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('934', '320282000000', '宜兴市', '3', '320200000000', '926', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('935', '320300000000', '徐州市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('936', '320301000000', '市辖区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('937', '320302000000', '鼓楼区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('938', '320303000000', '云龙区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('939', '320305000000', '贾汪区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('940', '320311000000', '泉山区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('941', '320312000000', '铜山区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('942', '320321000000', '丰县', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('943', '320322000000', '沛县', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('944', '320324000000', '睢宁县', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('945', '320371000000', '徐州经济技术开发区', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('946', '320381000000', '新沂市', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('947', '320382000000', '邳州市', '3', '320300000000', '935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('948', '320400000000', '常州市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('949', '320401000000', '市辖区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('950', '320402000000', '天宁区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('951', '320404000000', '钟楼区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('952', '320411000000', '新北区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('953', '320412000000', '武进区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('954', '320413000000', '金坛区', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('955', '320481000000', '溧阳市', '3', '320400000000', '948', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('956', '320500000000', '苏州市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('957', '320501000000', '市辖区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('958', '320505000000', '虎丘区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('959', '320506000000', '吴中区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('960', '320507000000', '相城区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('961', '320508000000', '姑苏区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('962', '320509000000', '吴江区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('963', '320571000000', '苏州工业园区', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('964', '320581000000', '常熟市', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('965', '320582000000', '张家港市', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('966', '320583000000', '昆山市', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('967', '320585000000', '太仓市', '3', '320500000000', '956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('968', '320600000000', '南通市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('969', '320601000000', '市辖区', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('970', '320612000000', '通州区', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('971', '320613000000', '崇川区', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('972', '320614000000', '海门区', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('973', '320623000000', '如东县', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('974', '320671000000', '南通经济技术开发区', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('975', '320681000000', '启东市', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('976', '320682000000', '如皋市', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('977', '320685000000', '海安市', '3', '320600000000', '968', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('978', '320700000000', '连云港市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('979', '320701000000', '市辖区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('980', '320703000000', '连云区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('981', '320706000000', '海州区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('982', '320707000000', '赣榆区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('983', '320722000000', '东海县', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('984', '320723000000', '灌云县', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('985', '320724000000', '灌南县', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('986', '320771000000', '连云港经济技术开发区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('987', '320772000000', '连云港高新技术产业开发区', '3', '320700000000', '978', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('988', '320800000000', '淮安市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('989', '320801000000', '市辖区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('990', '320803000000', '淮安区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('991', '320804000000', '淮阴区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('992', '320812000000', '清江浦区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('993', '320813000000', '洪泽区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('994', '320826000000', '涟水县', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('995', '320830000000', '盱眙县', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('996', '320831000000', '金湖县', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('997', '320871000000', '淮安经济技术开发区', '3', '320800000000', '988', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('998', '320900000000', '盐城市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('999', '320901000000', '市辖区', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1000', '320902000000', '亭湖区', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1001', '320903000000', '盐都区', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1002', '320904000000', '大丰区', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1003', '320921000000', '响水县', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1004', '320922000000', '滨海县', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1005', '320923000000', '阜宁县', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1006', '320924000000', '射阳县', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1007', '320925000000', '建湖县', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1008', '320971000000', '盐城经济技术开发区', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1009', '320981000000', '东台市', '3', '320900000000', '998', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1010', '321000000000', '扬州市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1011', '321001000000', '市辖区', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1012', '321002000000', '广陵区', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1013', '321003000000', '邗江区', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1014', '321012000000', '江都区', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1015', '321023000000', '宝应县', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1016', '321071000000', '扬州经济技术开发区', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1017', '321081000000', '仪征市', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1018', '321084000000', '高邮市', '3', '321000000000', '1010', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1019', '321100000000', '镇江市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1020', '321101000000', '市辖区', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1021', '321102000000', '京口区', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1022', '321111000000', '润州区', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1023', '321112000000', '丹徒区', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1024', '321171000000', '镇江新区', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1025', '321181000000', '丹阳市', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1026', '321182000000', '扬中市', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1027', '321183000000', '句容市', '3', '321100000000', '1019', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1028', '321200000000', '泰州市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1029', '321201000000', '市辖区', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1030', '321202000000', '海陵区', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1031', '321203000000', '高港区', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1032', '321204000000', '姜堰区', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1033', '321271000000', '泰州医药高新技术产业开发区', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('1034', '321281000000', '兴化市', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1035', '321282000000', '靖江市', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1036', '321283000000', '泰兴市', '3', '321200000000', '1028', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1037', '321300000000', '宿迁市', '2', '320000000000', '912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1038', '321301000000', '市辖区', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1039', '321302000000', '宿城区', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1040', '321311000000', '宿豫区', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1041', '321322000000', '沭阳县', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1042', '321323000000', '泗阳县', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1043', '321324000000', '泗洪县', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1044', '321371000000', '宿迁经济技术开发区', '3', '321300000000', '1037', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1045', '330000000000', '浙江省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1046', '330100000000', '杭州市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1047', '330101000000', '市辖区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1048', '330102000000', '上城区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1049', '330105000000', '拱墅区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1050', '330106000000', '西湖区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1051', '330108000000', '滨江区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1052', '330109000000', '萧山区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1053', '330110000000', '余杭区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1054', '330111000000', '富阳区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1055', '330112000000', '临安区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1056', '330113000000', '临平区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1057', '330114000000', '钱塘区', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1058', '330122000000', '桐庐县', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1059', '330127000000', '淳安县', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1060', '330182000000', '建德市', '3', '330100000000', '1046', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1061', '330200000000', '宁波市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1062', '330201000000', '市辖区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1063', '330203000000', '海曙区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1064', '330205000000', '江北区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1065', '330206000000', '北仑区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1066', '330211000000', '镇海区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1067', '330212000000', '鄞州区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1068', '330213000000', '奉化区', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1069', '330225000000', '象山县', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1070', '330226000000', '宁海县', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1071', '330281000000', '余姚市', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1072', '330282000000', '慈溪市', '3', '330200000000', '1061', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1073', '330300000000', '温州市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1074', '330301000000', '市辖区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1075', '330302000000', '鹿城区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1076', '330303000000', '龙湾区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1077', '330304000000', '瓯海区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1078', '330305000000', '洞头区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1079', '330324000000', '永嘉县', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1080', '330326000000', '平阳县', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1081', '330327000000', '苍南县', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1082', '330328000000', '文成县', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1083', '330329000000', '泰顺县', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1084', '330371000000', '温州经济技术开发区', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1085', '330381000000', '瑞安市', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1086', '330382000000', '乐清市', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1087', '330383000000', '龙港市', '3', '330300000000', '1073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1088', '330400000000', '嘉兴市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1089', '330401000000', '市辖区', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1090', '330402000000', '南湖区', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1091', '330411000000', '秀洲区', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1092', '330421000000', '嘉善县', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1093', '330424000000', '海盐县', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1094', '330481000000', '海宁市', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1095', '330482000000', '平湖市', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1096', '330483000000', '桐乡市', '3', '330400000000', '1088', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1097', '330500000000', '湖州市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1098', '330501000000', '市辖区', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1099', '330502000000', '吴兴区', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1100', '330503000000', '南浔区', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1101', '330521000000', '德清县', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1102', '330522000000', '长兴县', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1103', '330523000000', '安吉县', '3', '330500000000', '1097', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1104', '330600000000', '绍兴市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1105', '330601000000', '市辖区', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1106', '330602000000', '越城区', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1107', '330603000000', '柯桥区', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1108', '330604000000', '上虞区', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1109', '330624000000', '新昌县', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1110', '330681000000', '诸暨市', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1111', '330683000000', '嵊州市', '3', '330600000000', '1104', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1112', '330700000000', '金华市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1113', '330701000000', '市辖区', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1114', '330702000000', '婺城区', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1115', '330703000000', '金东区', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1116', '330723000000', '武义县', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1117', '330726000000', '浦江县', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1118', '330727000000', '磐安县', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1119', '330781000000', '兰溪市', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1120', '330782000000', '义乌市', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1121', '330783000000', '东阳市', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1122', '330784000000', '永康市', '3', '330700000000', '1112', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1123', '330800000000', '衢州市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1124', '330801000000', '市辖区', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1125', '330802000000', '柯城区', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1126', '330803000000', '衢江区', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1127', '330822000000', '常山县', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1128', '330824000000', '开化县', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1129', '330825000000', '龙游县', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1130', '330881000000', '江山市', '3', '330800000000', '1123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1131', '330900000000', '舟山市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1132', '330901000000', '市辖区', '3', '330900000000', '1131', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1133', '330902000000', '定海区', '3', '330900000000', '1131', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1134', '330903000000', '普陀区', '3', '330900000000', '1131', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1135', '330921000000', '岱山县', '3', '330900000000', '1131', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1136', '330922000000', '嵊泗县', '3', '330900000000', '1131', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1137', '331000000000', '台州市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1138', '331001000000', '市辖区', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1139', '331002000000', '椒江区', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1140', '331003000000', '黄岩区', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1141', '331004000000', '路桥区', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1142', '331022000000', '三门县', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1143', '331023000000', '天台县', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1144', '331024000000', '仙居县', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1145', '331081000000', '温岭市', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1146', '331082000000', '临海市', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1147', '331083000000', '玉环市', '3', '331000000000', '1137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1148', '331100000000', '丽水市', '2', '330000000000', '1045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1149', '331101000000', '市辖区', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1150', '331102000000', '莲都区', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1151', '331121000000', '青田县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1152', '331122000000', '缙云县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1153', '331123000000', '遂昌县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1154', '331124000000', '松阳县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1155', '331125000000', '云和县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1156', '331126000000', '庆元县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1157', '331127000000', '景宁畲族自治县', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1158', '331181000000', '龙泉市', '3', '331100000000', '1148', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1159', '340000000000', '安徽省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1160', '340100000000', '合肥市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1161', '340101000000', '市辖区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1162', '340102000000', '瑶海区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1163', '340103000000', '庐阳区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1164', '340104000000', '蜀山区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1165', '340111000000', '包河区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1166', '340121000000', '长丰县', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1167', '340122000000', '肥东县', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1168', '340123000000', '肥西县', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1169', '340124000000', '庐江县', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1170', '340171000000', '合肥高新技术产业开发区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1171', '340172000000', '合肥经济技术开发区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1172', '340173000000', '合肥新站高新技术产业开发区', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('1173', '340181000000', '巢湖市', '3', '340100000000', '1160', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1174', '340200000000', '芜湖市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1175', '340201000000', '市辖区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1176', '340202000000', '镜湖区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1177', '340207000000', '鸠江区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1178', '340209000000', '弋江区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1179', '340210000000', '湾沚区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1180', '340212000000', '繁昌区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1181', '340223000000', '南陵县', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1182', '340271000000', '芜湖经济技术开发区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1183', '340272000000', '安徽芜湖三山经济开发区', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1184', '340281000000', '无为市', '3', '340200000000', '1174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1185', '340300000000', '蚌埠市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1186', '340301000000', '市辖区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1187', '340302000000', '龙子湖区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1188', '340303000000', '蚌山区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1189', '340304000000', '禹会区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1190', '340311000000', '淮上区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1191', '340321000000', '怀远县', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1192', '340322000000', '五河县', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1193', '340323000000', '固镇县', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1194', '340371000000', '蚌埠市高新技术开发区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1195', '340372000000', '蚌埠市经济开发区', '3', '340300000000', '1185', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1196', '340400000000', '淮南市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1197', '340401000000', '市辖区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1198', '340402000000', '大通区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1199', '340403000000', '田家庵区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1200', '340404000000', '谢家集区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1201', '340405000000', '八公山区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1202', '340406000000', '潘集区', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1203', '340421000000', '凤台县', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1204', '340422000000', '寿县', '3', '340400000000', '1196', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1205', '340500000000', '马鞍山市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1206', '340501000000', '市辖区', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1207', '340503000000', '花山区', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1208', '340504000000', '雨山区', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1209', '340506000000', '博望区', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1210', '340521000000', '当涂县', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1211', '340522000000', '含山县', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1212', '340523000000', '和县', '3', '340500000000', '1205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1213', '340600000000', '淮北市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1214', '340601000000', '市辖区', '3', '340600000000', '1213', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1215', '340602000000', '杜集区', '3', '340600000000', '1213', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1216', '340603000000', '相山区', '3', '340600000000', '1213', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1217', '340604000000', '烈山区', '3', '340600000000', '1213', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1218', '340621000000', '濉溪县', '3', '340600000000', '1213', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1219', '340700000000', '铜陵市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1220', '340701000000', '市辖区', '3', '340700000000', '1219', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1221', '340705000000', '铜官区', '3', '340700000000', '1219', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1222', '340706000000', '义安区', '3', '340700000000', '1219', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1223', '340711000000', '郊区', '3', '340700000000', '1219', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1224', '340722000000', '枞阳县', '3', '340700000000', '1219', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1225', '340800000000', '安庆市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1226', '340801000000', '市辖区', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1227', '340802000000', '迎江区', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1228', '340803000000', '大观区', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1229', '340811000000', '宜秀区', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1230', '340822000000', '怀宁县', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1231', '340825000000', '太湖县', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1232', '340826000000', '宿松县', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1233', '340827000000', '望江县', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1234', '340828000000', '岳西县', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1235', '340871000000', '安徽安庆经济开发区', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1236', '340881000000', '桐城市', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1237', '340882000000', '潜山市', '3', '340800000000', '1225', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1238', '341000000000', '黄山市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1239', '341001000000', '市辖区', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1240', '341002000000', '屯溪区', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1241', '341003000000', '黄山区', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1242', '341004000000', '徽州区', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1243', '341021000000', '歙县', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1244', '341022000000', '休宁县', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1245', '341023000000', '黟县', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1246', '341024000000', '祁门县', '3', '341000000000', '1238', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1247', '341100000000', '滁州市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1248', '341101000000', '市辖区', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1249', '341102000000', '琅琊区', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1250', '341103000000', '南谯区', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1251', '341122000000', '来安县', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1252', '341124000000', '全椒县', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1253', '341125000000', '定远县', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1254', '341126000000', '凤阳县', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1255', '341171000000', '中新苏滁高新技术产业开发区', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('1256', '341172000000', '滁州经济技术开发区', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1257', '341181000000', '天长市', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1258', '341182000000', '明光市', '3', '341100000000', '1247', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1259', '341200000000', '阜阳市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1260', '341201000000', '市辖区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1261', '341202000000', '颍州区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1262', '341203000000', '颍东区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1263', '341204000000', '颍泉区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1264', '341221000000', '临泉县', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1265', '341222000000', '太和县', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1266', '341225000000', '阜南县', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1267', '341226000000', '颍上县', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1268', '341271000000', '阜阳合肥现代产业园区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1269', '341272000000', '阜阳经济技术开发区', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1270', '341282000000', '界首市', '3', '341200000000', '1259', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1271', '341300000000', '宿州市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1272', '341301000000', '市辖区', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1273', '341302000000', '埇桥区', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1274', '341321000000', '砀山县', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1275', '341322000000', '萧县', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1276', '341323000000', '灵璧县', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1277', '341324000000', '泗县', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1278', '341371000000', '宿州马鞍山现代产业园区', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1279', '341372000000', '宿州经济技术开发区', '3', '341300000000', '1271', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1280', '341500000000', '六安市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1281', '341501000000', '市辖区', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1282', '341502000000', '金安区', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1283', '341503000000', '裕安区', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1284', '341504000000', '叶集区', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1285', '341522000000', '霍邱县', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1286', '341523000000', '舒城县', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1287', '341524000000', '金寨县', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1288', '341525000000', '霍山县', '3', '341500000000', '1280', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1289', '341600000000', '亳州市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1290', '341601000000', '市辖区', '3', '341600000000', '1289', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1291', '341602000000', '谯城区', '3', '341600000000', '1289', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1292', '341621000000', '涡阳县', '3', '341600000000', '1289', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1293', '341622000000', '蒙城县', '3', '341600000000', '1289', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1294', '341623000000', '利辛县', '3', '341600000000', '1289', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1295', '341700000000', '池州市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1296', '341701000000', '市辖区', '3', '341700000000', '1295', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1297', '341702000000', '贵池区', '3', '341700000000', '1295', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1298', '341721000000', '东至县', '3', '341700000000', '1295', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1299', '341722000000', '石台县', '3', '341700000000', '1295', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1300', '341723000000', '青阳县', '3', '341700000000', '1295', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1301', '341800000000', '宣城市', '2', '340000000000', '1159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1302', '341801000000', '市辖区', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1303', '341802000000', '宣州区', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1304', '341821000000', '郎溪县', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1305', '341823000000', '泾县', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1306', '341824000000', '绩溪县', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1307', '341825000000', '旌德县', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1308', '341871000000', '宣城市经济开发区', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1309', '341881000000', '宁国市', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1310', '341882000000', '广德市', '3', '341800000000', '1301', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1311', '350000000000', '福建省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1312', '350100000000', '福州市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1313', '350101000000', '市辖区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1314', '350102000000', '鼓楼区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1315', '350103000000', '台江区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1316', '350104000000', '仓山区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1317', '350105000000', '马尾区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1318', '350111000000', '晋安区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1319', '350112000000', '长乐区', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1320', '350121000000', '闽侯县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1321', '350122000000', '连江县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1322', '350123000000', '罗源县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1323', '350124000000', '闽清县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1324', '350125000000', '永泰县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1325', '350128000000', '平潭县', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1326', '350181000000', '福清市', '3', '350100000000', '1312', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1327', '350200000000', '厦门市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1328', '350201000000', '市辖区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1329', '350203000000', '思明区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1330', '350205000000', '海沧区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1331', '350206000000', '湖里区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1332', '350211000000', '集美区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1333', '350212000000', '同安区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1334', '350213000000', '翔安区', '3', '350200000000', '1327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1335', '350300000000', '莆田市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1336', '350301000000', '市辖区', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1337', '350302000000', '城厢区', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1338', '350303000000', '涵江区', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1339', '350304000000', '荔城区', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1340', '350305000000', '秀屿区', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1341', '350322000000', '仙游县', '3', '350300000000', '1335', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1342', '350400000000', '三明市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1343', '350401000000', '市辖区', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1344', '350404000000', '三元区', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1345', '350405000000', '沙县区', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1346', '350421000000', '明溪县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1347', '350423000000', '清流县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1348', '350424000000', '宁化县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1349', '350425000000', '大田县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1350', '350426000000', '尤溪县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1351', '350428000000', '将乐县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1352', '350429000000', '泰宁县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1353', '350430000000', '建宁县', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1354', '350481000000', '永安市', '3', '350400000000', '1342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1355', '350500000000', '泉州市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1356', '350501000000', '市辖区', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1357', '350502000000', '鲤城区', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1358', '350503000000', '丰泽区', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1359', '350504000000', '洛江区', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1360', '350505000000', '泉港区', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1361', '350521000000', '惠安县', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1362', '350524000000', '安溪县', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1363', '350525000000', '永春县', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1364', '350526000000', '德化县', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1365', '350527000000', '金门县', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1366', '350581000000', '石狮市', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1367', '350582000000', '晋江市', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1368', '350583000000', '南安市', '3', '350500000000', '1355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1369', '350600000000', '漳州市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1370', '350601000000', '市辖区', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1371', '350602000000', '芗城区', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1372', '350603000000', '龙文区', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1373', '350604000000', '龙海区', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1374', '350605000000', '长泰区', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1375', '350622000000', '云霄县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1376', '350623000000', '漳浦县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1377', '350624000000', '诏安县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1378', '350626000000', '东山县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1379', '350627000000', '南靖县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1380', '350628000000', '平和县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1381', '350629000000', '华安县', '3', '350600000000', '1369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1382', '350700000000', '南平市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1383', '350701000000', '市辖区', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1384', '350702000000', '延平区', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1385', '350703000000', '建阳区', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1386', '350721000000', '顺昌县', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1387', '350722000000', '浦城县', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1388', '350723000000', '光泽县', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1389', '350724000000', '松溪县', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1390', '350725000000', '政和县', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1391', '350781000000', '邵武市', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1392', '350782000000', '武夷山市', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1393', '350783000000', '建瓯市', '3', '350700000000', '1382', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1394', '350800000000', '龙岩市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1395', '350801000000', '市辖区', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1396', '350802000000', '新罗区', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1397', '350803000000', '永定区', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1398', '350821000000', '长汀县', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1399', '350823000000', '上杭县', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1400', '350824000000', '武平县', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1401', '350825000000', '连城县', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1402', '350881000000', '漳平市', '3', '350800000000', '1394', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1403', '350900000000', '宁德市', '2', '350000000000', '1311', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1404', '350901000000', '市辖区', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1405', '350902000000', '蕉城区', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1406', '350921000000', '霞浦县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1407', '350922000000', '古田县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1408', '350923000000', '屏南县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1409', '350924000000', '寿宁县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1410', '350925000000', '周宁县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1411', '350926000000', '柘荣县', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1412', '350981000000', '福安市', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1413', '350982000000', '福鼎市', '3', '350900000000', '1403', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1414', '360000000000', '江西省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1415', '360100000000', '南昌市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1416', '360101000000', '市辖区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1417', '360102000000', '东湖区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1418', '360103000000', '西湖区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1419', '360104000000', '青云谱区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1420', '360111000000', '青山湖区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1421', '360112000000', '新建区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1422', '360113000000', '红谷滩区', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1423', '360121000000', '南昌县', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1424', '360123000000', '安义县', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1425', '360124000000', '进贤县', '3', '360100000000', '1415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1426', '360200000000', '景德镇市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1427', '360201000000', '市辖区', '3', '360200000000', '1426', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1428', '360202000000', '昌江区', '3', '360200000000', '1426', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1429', '360203000000', '珠山区', '3', '360200000000', '1426', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1430', '360222000000', '浮梁县', '3', '360200000000', '1426', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1431', '360281000000', '乐平市', '3', '360200000000', '1426', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1432', '360300000000', '萍乡市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1433', '360301000000', '市辖区', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1434', '360302000000', '安源区', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1435', '360313000000', '湘东区', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1436', '360321000000', '莲花县', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1437', '360322000000', '上栗县', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1438', '360323000000', '芦溪县', '3', '360300000000', '1432', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1439', '360400000000', '九江市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1440', '360401000000', '市辖区', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1441', '360402000000', '濂溪区', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1442', '360403000000', '浔阳区', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1443', '360404000000', '柴桑区', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1444', '360423000000', '武宁县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1445', '360424000000', '修水县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1446', '360425000000', '永修县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1447', '360426000000', '德安县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1448', '360428000000', '都昌县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1449', '360429000000', '湖口县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1450', '360430000000', '彭泽县', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1451', '360481000000', '瑞昌市', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1452', '360482000000', '共青城市', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1453', '360483000000', '庐山市', '3', '360400000000', '1439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1454', '360500000000', '新余市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1455', '360501000000', '市辖区', '3', '360500000000', '1454', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1456', '360502000000', '渝水区', '3', '360500000000', '1454', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1457', '360521000000', '分宜县', '3', '360500000000', '1454', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1458', '360600000000', '鹰潭市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1459', '360601000000', '市辖区', '3', '360600000000', '1458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1460', '360602000000', '月湖区', '3', '360600000000', '1458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1461', '360603000000', '余江区', '3', '360600000000', '1458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1462', '360681000000', '贵溪市', '3', '360600000000', '1458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1463', '360700000000', '赣州市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1464', '360701000000', '市辖区', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1465', '360702000000', '章贡区', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1466', '360703000000', '南康区', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1467', '360704000000', '赣县区', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1468', '360722000000', '信丰县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1469', '360723000000', '大余县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1470', '360724000000', '上犹县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1471', '360725000000', '崇义县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1472', '360726000000', '安远县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1473', '360728000000', '定南县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1474', '360729000000', '全南县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1475', '360730000000', '宁都县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1476', '360731000000', '于都县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1477', '360732000000', '兴国县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1478', '360733000000', '会昌县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1479', '360734000000', '寻乌县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1480', '360735000000', '石城县', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1481', '360781000000', '瑞金市', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1482', '360783000000', '龙南市', '3', '360700000000', '1463', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1483', '360800000000', '吉安市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1484', '360801000000', '市辖区', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1485', '360802000000', '吉州区', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1486', '360803000000', '青原区', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1487', '360821000000', '吉安县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1488', '360822000000', '吉水县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1489', '360823000000', '峡江县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1490', '360824000000', '新干县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1491', '360825000000', '永丰县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1492', '360826000000', '泰和县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1493', '360827000000', '遂川县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1494', '360828000000', '万安县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1495', '360829000000', '安福县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1496', '360830000000', '永新县', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1497', '360881000000', '井冈山市', '3', '360800000000', '1483', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1498', '360900000000', '宜春市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1499', '360901000000', '市辖区', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1500', '360902000000', '袁州区', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1501', '360921000000', '奉新县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1502', '360922000000', '万载县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1503', '360923000000', '上高县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1504', '360924000000', '宜丰县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1505', '360925000000', '靖安县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1506', '360926000000', '铜鼓县', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1507', '360981000000', '丰城市', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1508', '360982000000', '樟树市', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1509', '360983000000', '高安市', '3', '360900000000', '1498', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1510', '361000000000', '抚州市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1511', '361001000000', '市辖区', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1512', '361002000000', '临川区', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1513', '361003000000', '东乡区', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1514', '361021000000', '南城县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1515', '361022000000', '黎川县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1516', '361023000000', '南丰县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1517', '361024000000', '崇仁县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1518', '361025000000', '乐安县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1519', '361026000000', '宜黄县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1520', '361027000000', '金溪县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1521', '361028000000', '资溪县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1522', '361030000000', '广昌县', '3', '361000000000', '1510', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1523', '361100000000', '上饶市', '2', '360000000000', '1414', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1524', '361101000000', '市辖区', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1525', '361102000000', '信州区', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1526', '361103000000', '广丰区', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1527', '361104000000', '广信区', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1528', '361123000000', '玉山县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1529', '361124000000', '铅山县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1530', '361125000000', '横峰县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1531', '361126000000', '弋阳县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1532', '361127000000', '余干县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1533', '361128000000', '鄱阳县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1534', '361129000000', '万年县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1535', '361130000000', '婺源县', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1536', '361181000000', '德兴市', '3', '361100000000', '1523', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1537', '370000000000', '山东省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1538', '370100000000', '济南市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1539', '370101000000', '市辖区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1540', '370102000000', '历下区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1541', '370103000000', '市中区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1542', '370104000000', '槐荫区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1543', '370105000000', '天桥区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1544', '370112000000', '历城区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1545', '370113000000', '长清区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1546', '370114000000', '章丘区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1547', '370115000000', '济阳区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1548', '370116000000', '莱芜区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1549', '370117000000', '钢城区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1550', '370124000000', '平阴县', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1551', '370126000000', '商河县', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1552', '370171000000', '济南高新技术产业开发区', '3', '370100000000', '1538', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1553', '370200000000', '青岛市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1554', '370201000000', '市辖区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1555', '370202000000', '市南区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1556', '370203000000', '市北区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1557', '370211000000', '黄岛区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1558', '370212000000', '崂山区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1559', '370213000000', '李沧区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1560', '370214000000', '城阳区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1561', '370215000000', '即墨区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1562', '370271000000', '青岛高新技术产业开发区', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1563', '370281000000', '胶州市', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1564', '370283000000', '平度市', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1565', '370285000000', '莱西市', '3', '370200000000', '1553', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1566', '370300000000', '淄博市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1567', '370301000000', '市辖区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1568', '370302000000', '淄川区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1569', '370303000000', '张店区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1570', '370304000000', '博山区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1571', '370305000000', '临淄区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1572', '370306000000', '周村区', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1573', '370321000000', '桓台县', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1574', '370322000000', '高青县', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1575', '370323000000', '沂源县', '3', '370300000000', '1566', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1576', '370400000000', '枣庄市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1577', '370401000000', '市辖区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1578', '370402000000', '市中区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1579', '370403000000', '薛城区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1580', '370404000000', '峄城区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1581', '370405000000', '台儿庄区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1582', '370406000000', '山亭区', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1583', '370481000000', '滕州市', '3', '370400000000', '1576', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1584', '370500000000', '东营市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1585', '370501000000', '市辖区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1586', '370502000000', '东营区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1587', '370503000000', '河口区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1588', '370505000000', '垦利区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1589', '370522000000', '利津县', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1590', '370523000000', '广饶县', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1591', '370571000000', '东营经济技术开发区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1592', '370572000000', '东营港经济开发区', '3', '370500000000', '1584', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1593', '370600000000', '烟台市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1594', '370601000000', '市辖区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1595', '370602000000', '芝罘区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1596', '370611000000', '福山区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1597', '370612000000', '牟平区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1598', '370613000000', '莱山区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1599', '370614000000', '蓬莱区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1600', '370671000000', '烟台高新技术产业开发区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1601', '370672000000', '烟台经济技术开发区', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1602', '370681000000', '龙口市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1603', '370682000000', '莱阳市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1604', '370683000000', '莱州市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1605', '370685000000', '招远市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1606', '370686000000', '栖霞市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1607', '370687000000', '海阳市', '3', '370600000000', '1593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1608', '370700000000', '潍坊市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1609', '370701000000', '市辖区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1610', '370702000000', '潍城区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1611', '370703000000', '寒亭区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1612', '370704000000', '坊子区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1613', '370705000000', '奎文区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1614', '370724000000', '临朐县', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1615', '370725000000', '昌乐县', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1616', '370772000000', '潍坊滨海经济技术开发区', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1617', '370781000000', '青州市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1618', '370782000000', '诸城市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1619', '370783000000', '寿光市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1620', '370784000000', '安丘市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1621', '370785000000', '高密市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1622', '370786000000', '昌邑市', '3', '370700000000', '1608', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1623', '370800000000', '济宁市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1624', '370801000000', '市辖区', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1625', '370811000000', '任城区', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1626', '370812000000', '兖州区', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1627', '370826000000', '微山县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1628', '370827000000', '鱼台县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1629', '370828000000', '金乡县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1630', '370829000000', '嘉祥县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1631', '370830000000', '汶上县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1632', '370831000000', '泗水县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1633', '370832000000', '梁山县', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1634', '370871000000', '济宁高新技术产业开发区', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1635', '370881000000', '曲阜市', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1636', '370883000000', '邹城市', '3', '370800000000', '1623', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1637', '370900000000', '泰安市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1638', '370901000000', '市辖区', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1639', '370902000000', '泰山区', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1640', '370911000000', '岱岳区', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1641', '370921000000', '宁阳县', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1642', '370923000000', '东平县', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1643', '370982000000', '新泰市', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1644', '370983000000', '肥城市', '3', '370900000000', '1637', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1645', '371000000000', '威海市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1646', '371001000000', '市辖区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1647', '371002000000', '环翠区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1648', '371003000000', '文登区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1649', '371071000000', '威海火炬高技术产业开发区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1650', '371072000000', '威海经济技术开发区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1651', '371073000000', '威海临港经济技术开发区', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1652', '371082000000', '荣成市', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1653', '371083000000', '乳山市', '3', '371000000000', '1645', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1654', '371100000000', '日照市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1655', '371101000000', '市辖区', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1656', '371102000000', '东港区', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1657', '371103000000', '岚山区', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1658', '371121000000', '五莲县', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1659', '371122000000', '莒县', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1660', '371171000000', '日照经济技术开发区', '3', '371100000000', '1654', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1661', '371300000000', '临沂市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1662', '371301000000', '市辖区', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1663', '371302000000', '兰山区', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1664', '371311000000', '罗庄区', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1665', '371312000000', '河东区', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1666', '371321000000', '沂南县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1667', '371322000000', '郯城县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1668', '371323000000', '沂水县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1669', '371324000000', '兰陵县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1670', '371325000000', '费县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1671', '371326000000', '平邑县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1672', '371327000000', '莒南县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1673', '371328000000', '蒙阴县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1674', '371329000000', '临沭县', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1675', '371371000000', '临沂高新技术产业开发区', '3', '371300000000', '1661', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1676', '371400000000', '德州市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1677', '371401000000', '市辖区', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1678', '371402000000', '德城区', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1679', '371403000000', '陵城区', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1680', '371422000000', '宁津县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1681', '371423000000', '庆云县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1682', '371424000000', '临邑县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1683', '371425000000', '齐河县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1684', '371426000000', '平原县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1685', '371427000000', '夏津县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1686', '371428000000', '武城县', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1687', '371471000000', '德州经济技术开发区', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1688', '371472000000', '德州运河经济开发区', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1689', '371481000000', '乐陵市', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1690', '371482000000', '禹城市', '3', '371400000000', '1676', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1691', '371500000000', '聊城市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1692', '371501000000', '市辖区', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1693', '371502000000', '东昌府区', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1694', '371503000000', '茌平区', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1695', '371521000000', '阳谷县', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1696', '371522000000', '莘县', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1697', '371524000000', '东阿县', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1698', '371525000000', '冠县', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1699', '371526000000', '高唐县', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1700', '371581000000', '临清市', '3', '371500000000', '1691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1701', '371600000000', '滨州市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1702', '371601000000', '市辖区', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1703', '371602000000', '滨城区', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1704', '371603000000', '沾化区', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1705', '371621000000', '惠民县', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1706', '371622000000', '阳信县', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1707', '371623000000', '无棣县', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1708', '371625000000', '博兴县', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1709', '371681000000', '邹平市', '3', '371600000000', '1701', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1710', '371700000000', '菏泽市', '2', '370000000000', '1537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1711', '371701000000', '市辖区', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1712', '371702000000', '牡丹区', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1713', '371703000000', '定陶区', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1714', '371721000000', '曹县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1715', '371722000000', '单县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1716', '371723000000', '成武县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1717', '371724000000', '巨野县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1718', '371725000000', '郓城县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1719', '371726000000', '鄄城县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1720', '371728000000', '东明县', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1721', '371771000000', '菏泽经济技术开发区', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1722', '371772000000', '菏泽高新技术开发区', '3', '371700000000', '1710', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1723', '410000000000', '河南省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1724', '410100000000', '郑州市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1725', '410101000000', '市辖区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1726', '410102000000', '中原区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1727', '410103000000', '二七区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1728', '410104000000', '管城回族区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1729', '410105000000', '金水区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1730', '410106000000', '上街区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1731', '410108000000', '惠济区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1732', '410122000000', '中牟县', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1733', '410171000000', '郑州经济技术开发区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1734', '410172000000', '郑州高新技术产业开发区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1735', '410173000000', '郑州航空港经济综合实验区', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1736', '410181000000', '巩义市', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1737', '410182000000', '荥阳市', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1738', '410183000000', '新密市', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1739', '410184000000', '新郑市', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1740', '410185000000', '登封市', '3', '410100000000', '1724', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1741', '410200000000', '开封市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1742', '410201000000', '市辖区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1743', '410202000000', '龙亭区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1744', '410203000000', '顺河回族区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1745', '410204000000', '鼓楼区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1746', '410205000000', '禹王台区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1747', '410212000000', '祥符区', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1748', '410221000000', '杞县', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1749', '410222000000', '通许县', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1750', '410223000000', '尉氏县', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1751', '410225000000', '兰考县', '3', '410200000000', '1741', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1752', '410300000000', '洛阳市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1753', '410301000000', '市辖区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1754', '410302000000', '老城区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1755', '410303000000', '西工区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1756', '410304000000', '瀍河回族区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1757', '410305000000', '涧西区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1758', '410307000000', '偃师区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1759', '410308000000', '孟津区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1760', '410311000000', '洛龙区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1761', '410323000000', '新安县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1762', '410324000000', '栾川县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1763', '410325000000', '嵩县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1764', '410326000000', '汝阳县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1765', '410327000000', '宜阳县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1766', '410328000000', '洛宁县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1767', '410329000000', '伊川县', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1768', '410371000000', '洛阳高新技术产业开发区', '3', '410300000000', '1752', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1769', '410400000000', '平顶山市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1770', '410401000000', '市辖区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1771', '410402000000', '新华区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1772', '410403000000', '卫东区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1773', '410404000000', '石龙区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1774', '410411000000', '湛河区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1775', '410421000000', '宝丰县', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1776', '410422000000', '叶县', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1777', '410423000000', '鲁山县', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1778', '410425000000', '郏县', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1779', '410471000000', '平顶山高新技术产业开发区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1780', '410472000000', '平顶山市城乡一体化示范区', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1781', '410481000000', '舞钢市', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1782', '410482000000', '汝州市', '3', '410400000000', '1769', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1783', '410500000000', '安阳市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1784', '410501000000', '市辖区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1785', '410502000000', '文峰区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1786', '410503000000', '北关区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1787', '410505000000', '殷都区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1788', '410506000000', '龙安区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1789', '410522000000', '安阳县', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1790', '410523000000', '汤阴县', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1791', '410526000000', '滑县', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1792', '410527000000', '内黄县', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1793', '410571000000', '安阳高新技术产业开发区', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1794', '410581000000', '林州市', '3', '410500000000', '1783', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1795', '410600000000', '鹤壁市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1796', '410601000000', '市辖区', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1797', '410602000000', '鹤山区', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1798', '410603000000', '山城区', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1799', '410611000000', '淇滨区', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1800', '410621000000', '浚县', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1801', '410622000000', '淇县', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1802', '410671000000', '鹤壁经济技术开发区', '3', '410600000000', '1795', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1803', '410700000000', '新乡市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1804', '410701000000', '市辖区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1805', '410702000000', '红旗区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1806', '410703000000', '卫滨区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1807', '410704000000', '凤泉区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1808', '410711000000', '牧野区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1809', '410721000000', '新乡县', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1810', '410724000000', '获嘉县', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1811', '410725000000', '原阳县', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1812', '410726000000', '延津县', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1813', '410727000000', '封丘县', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1814', '410771000000', '新乡高新技术产业开发区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1815', '410772000000', '新乡经济技术开发区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1816', '410773000000', '新乡市平原城乡一体化示范区', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('1817', '410781000000', '卫辉市', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1818', '410782000000', '辉县市', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1819', '410783000000', '长垣市', '3', '410700000000', '1803', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1820', '410800000000', '焦作市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1821', '410801000000', '市辖区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1822', '410802000000', '解放区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1823', '410803000000', '中站区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1824', '410804000000', '马村区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1825', '410811000000', '山阳区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1826', '410821000000', '修武县', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1827', '410822000000', '博爱县', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1828', '410823000000', '武陟县', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1829', '410825000000', '温县', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1830', '410871000000', '焦作城乡一体化示范区', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1831', '410882000000', '沁阳市', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1832', '410883000000', '孟州市', '3', '410800000000', '1820', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1833', '410900000000', '濮阳市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1834', '410901000000', '市辖区', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1835', '410902000000', '华龙区', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1836', '410922000000', '清丰县', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1837', '410923000000', '南乐县', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1838', '410926000000', '范县', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1839', '410927000000', '台前县', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1840', '410928000000', '濮阳县', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1841', '410971000000', '河南濮阳工业园区', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1842', '410972000000', '濮阳经济技术开发区', '3', '410900000000', '1833', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1843', '411000000000', '许昌市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1844', '411001000000', '市辖区', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1845', '411002000000', '魏都区', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1846', '411003000000', '建安区', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1847', '411024000000', '鄢陵县', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1848', '411025000000', '襄城县', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1849', '411071000000', '许昌经济技术开发区', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1850', '411081000000', '禹州市', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1851', '411082000000', '长葛市', '3', '411000000000', '1843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1852', '411100000000', '漯河市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1853', '411101000000', '市辖区', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1854', '411102000000', '源汇区', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1855', '411103000000', '郾城区', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1856', '411104000000', '召陵区', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1857', '411121000000', '舞阳县', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1858', '411122000000', '临颍县', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1859', '411171000000', '漯河经济技术开发区', '3', '411100000000', '1852', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1860', '411200000000', '三门峡市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1861', '411201000000', '市辖区', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1862', '411202000000', '湖滨区', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1863', '411203000000', '陕州区', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1864', '411221000000', '渑池县', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1865', '411224000000', '卢氏县', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1866', '411271000000', '河南三门峡经济开发区', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1867', '411281000000', '义马市', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1868', '411282000000', '灵宝市', '3', '411200000000', '1860', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1869', '411300000000', '南阳市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1870', '411301000000', '市辖区', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1871', '411302000000', '宛城区', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1872', '411303000000', '卧龙区', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1873', '411321000000', '南召县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1874', '411322000000', '方城县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1875', '411323000000', '西峡县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1876', '411324000000', '镇平县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1877', '411325000000', '内乡县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1878', '411326000000', '淅川县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1879', '411327000000', '社旗县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1880', '411328000000', '唐河县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1881', '411329000000', '新野县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1882', '411330000000', '桐柏县', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1883', '411371000000', '南阳高新技术产业开发区', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1884', '411372000000', '南阳市城乡一体化示范区', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1885', '411381000000', '邓州市', '3', '411300000000', '1869', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1886', '411400000000', '商丘市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1887', '411401000000', '市辖区', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1888', '411402000000', '梁园区', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1889', '411403000000', '睢阳区', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1890', '411421000000', '民权县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1891', '411422000000', '睢县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1892', '411423000000', '宁陵县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1893', '411424000000', '柘城县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1894', '411425000000', '虞城县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1895', '411426000000', '夏邑县', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1896', '411471000000', '豫东综合物流产业聚集区', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1897', '411472000000', '河南商丘经济开发区', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1898', '411481000000', '永城市', '3', '411400000000', '1886', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1899', '411500000000', '信阳市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1900', '411501000000', '市辖区', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1901', '411502000000', '浉河区', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1902', '411503000000', '平桥区', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1903', '411521000000', '罗山县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1904', '411522000000', '光山县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1905', '411523000000', '新县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1906', '411524000000', '商城县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1907', '411525000000', '固始县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1908', '411526000000', '潢川县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1909', '411527000000', '淮滨县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1910', '411528000000', '息县', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1911', '411571000000', '信阳高新技术产业开发区', '3', '411500000000', '1899', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1912', '411600000000', '周口市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1913', '411601000000', '市辖区', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1914', '411602000000', '川汇区', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1915', '411603000000', '淮阳区', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1916', '411621000000', '扶沟县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1917', '411622000000', '西华县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1918', '411623000000', '商水县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1919', '411624000000', '沈丘县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1920', '411625000000', '郸城县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1921', '411627000000', '太康县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1922', '411628000000', '鹿邑县', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1923', '411671000000', '河南周口经济开发区', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1924', '411681000000', '项城市', '3', '411600000000', '1912', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1925', '411700000000', '驻马店市', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1926', '411701000000', '市辖区', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1927', '411702000000', '驿城区', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1928', '411721000000', '西平县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1929', '411722000000', '上蔡县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1930', '411723000000', '平舆县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1931', '411724000000', '正阳县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1932', '411725000000', '确山县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1933', '411726000000', '泌阳县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1934', '411727000000', '汝南县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1935', '411728000000', '遂平县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1936', '411729000000', '新蔡县', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1937', '411771000000', '河南驻马店经济开发区', '3', '411700000000', '1925', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1938', '419000000000', '省直辖县级行政区划', '2', '410000000000', '1723', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1939', '419001000000', '济源市', '3', '419000000000', '1938', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1940', '420000000000', '湖北省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1941', '420100000000', '武汉市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1942', '420101000000', '市辖区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1943', '420102000000', '江岸区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1944', '420103000000', '江汉区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1945', '420104000000', '硚口区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1946', '420105000000', '汉阳区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1947', '420106000000', '武昌区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1948', '420107000000', '青山区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1949', '420111000000', '洪山区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1950', '420112000000', '东西湖区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1951', '420113000000', '汉南区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1952', '420114000000', '蔡甸区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1953', '420115000000', '江夏区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1954', '420116000000', '黄陂区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1955', '420117000000', '新洲区', '3', '420100000000', '1941', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1956', '420200000000', '黄石市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1957', '420201000000', '市辖区', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1958', '420202000000', '黄石港区', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1959', '420203000000', '西塞山区', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1960', '420204000000', '下陆区', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1961', '420205000000', '铁山区', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1962', '420222000000', '阳新县', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1963', '420281000000', '大冶市', '3', '420200000000', '1956', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1964', '420300000000', '十堰市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1965', '420301000000', '市辖区', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1966', '420302000000', '茅箭区', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1967', '420303000000', '张湾区', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1968', '420304000000', '郧阳区', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1969', '420322000000', '郧西县', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1970', '420323000000', '竹山县', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1971', '420324000000', '竹溪县', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1972', '420325000000', '房县', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1973', '420381000000', '丹江口市', '3', '420300000000', '1964', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1974', '420500000000', '宜昌市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1975', '420501000000', '市辖区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1976', '420502000000', '西陵区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1977', '420503000000', '伍家岗区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1978', '420504000000', '点军区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1979', '420505000000', '猇亭区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1980', '420506000000', '夷陵区', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1981', '420525000000', '远安县', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1982', '420526000000', '兴山县', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1983', '420527000000', '秭归县', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1984', '420528000000', '长阳土家族自治县', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1985', '420529000000', '五峰土家族自治县', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('1986', '420581000000', '宜都市', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1987', '420582000000', '当阳市', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1988', '420583000000', '枝江市', '3', '420500000000', '1974', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1989', '420600000000', '襄阳市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1990', '420601000000', '市辖区', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1991', '420602000000', '襄城区', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1992', '420606000000', '樊城区', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1993', '420607000000', '襄州区', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1994', '420624000000', '南漳县', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1995', '420625000000', '谷城县', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1996', '420626000000', '保康县', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1997', '420682000000', '老河口市', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1998', '420683000000', '枣阳市', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('1999', '420684000000', '宜城市', '3', '420600000000', '1989', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2000', '420700000000', '鄂州市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2001', '420701000000', '市辖区', '3', '420700000000', '2000', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2002', '420702000000', '梁子湖区', '3', '420700000000', '2000', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2003', '420703000000', '华容区', '3', '420700000000', '2000', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2004', '420704000000', '鄂城区', '3', '420700000000', '2000', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2005', '420800000000', '荆门市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2006', '420801000000', '市辖区', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2007', '420802000000', '东宝区', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2008', '420804000000', '掇刀区', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2009', '420822000000', '沙洋县', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2010', '420881000000', '钟祥市', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2011', '420882000000', '京山市', '3', '420800000000', '2005', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2012', '420900000000', '孝感市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2013', '420901000000', '市辖区', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2014', '420902000000', '孝南区', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2015', '420921000000', '孝昌县', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2016', '420922000000', '大悟县', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2017', '420923000000', '云梦县', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2018', '420981000000', '应城市', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2019', '420982000000', '安陆市', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2020', '420984000000', '汉川市', '3', '420900000000', '2012', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2021', '421000000000', '荆州市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2022', '421001000000', '市辖区', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2023', '421002000000', '沙市区', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2024', '421003000000', '荆州区', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2025', '421022000000', '公安县', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2026', '421024000000', '江陵县', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2027', '421071000000', '荆州经济技术开发区', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2028', '421081000000', '石首市', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2029', '421083000000', '洪湖市', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2030', '421087000000', '松滋市', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2031', '421088000000', '监利市', '3', '421000000000', '2021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2032', '421100000000', '黄冈市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2033', '421101000000', '市辖区', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2034', '421102000000', '黄州区', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2035', '421121000000', '团风县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2036', '421122000000', '红安县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2037', '421123000000', '罗田县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2038', '421124000000', '英山县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2039', '421125000000', '浠水县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2040', '421126000000', '蕲春县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2041', '421127000000', '黄梅县', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2042', '421171000000', '龙感湖管理区', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2043', '421181000000', '麻城市', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2044', '421182000000', '武穴市', '3', '421100000000', '2032', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2045', '421200000000', '咸宁市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2046', '421201000000', '市辖区', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2047', '421202000000', '咸安区', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2048', '421221000000', '嘉鱼县', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2049', '421222000000', '通城县', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2050', '421223000000', '崇阳县', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2051', '421224000000', '通山县', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2052', '421281000000', '赤壁市', '3', '421200000000', '2045', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2053', '421300000000', '随州市', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2054', '421301000000', '市辖区', '3', '421300000000', '2053', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2055', '421303000000', '曾都区', '3', '421300000000', '2053', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2056', '421321000000', '随县', '3', '421300000000', '2053', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2057', '421381000000', '广水市', '3', '421300000000', '2053', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2058', '422800000000', '恩施土家族苗族自治州', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2059', '422801000000', '恩施市', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2060', '422802000000', '利川市', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2061', '422822000000', '建始县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2062', '422823000000', '巴东县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2063', '422825000000', '宣恩县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2064', '422826000000', '咸丰县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2065', '422827000000', '来凤县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2066', '422828000000', '鹤峰县', '3', '422800000000', '2058', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2067', '429000000000', '省直辖县级行政区划', '2', '420000000000', '1940', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2068', '429004000000', '仙桃市', '3', '429000000000', '2067', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2069', '429005000000', '潜江市', '3', '429000000000', '2067', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2070', '429006000000', '天门市', '3', '429000000000', '2067', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2071', '429021000000', '神农架林区', '3', '429000000000', '2067', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2072', '430000000000', '湖南省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2073', '430100000000', '长沙市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2074', '430101000000', '市辖区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2075', '430102000000', '芙蓉区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2076', '430103000000', '天心区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2077', '430104000000', '岳麓区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2078', '430105000000', '开福区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2079', '430111000000', '雨花区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2080', '430112000000', '望城区', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2081', '430121000000', '长沙县', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2082', '430181000000', '浏阳市', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2083', '430182000000', '宁乡市', '3', '430100000000', '2073', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2084', '430200000000', '株洲市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2085', '430201000000', '市辖区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2086', '430202000000', '荷塘区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2087', '430203000000', '芦淞区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2088', '430204000000', '石峰区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2089', '430211000000', '天元区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2090', '430212000000', '渌口区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2091', '430223000000', '攸县', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2092', '430224000000', '茶陵县', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2093', '430225000000', '炎陵县', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2094', '430271000000', '云龙示范区', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2095', '430281000000', '醴陵市', '3', '430200000000', '2084', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2096', '430300000000', '湘潭市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2097', '430301000000', '市辖区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2098', '430302000000', '雨湖区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2099', '430304000000', '岳塘区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2100', '430321000000', '湘潭县', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2101', '430371000000', '湖南湘潭高新技术产业园区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2102', '430372000000', '湘潭昭山示范区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2103', '430373000000', '湘潭九华示范区', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2104', '430381000000', '湘乡市', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2105', '430382000000', '韶山市', '3', '430300000000', '2096', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2106', '430400000000', '衡阳市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2107', '430401000000', '市辖区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2108', '430405000000', '珠晖区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2109', '430406000000', '雁峰区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2110', '430407000000', '石鼓区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2111', '430408000000', '蒸湘区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2112', '430412000000', '南岳区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2113', '430421000000', '衡阳县', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2114', '430422000000', '衡南县', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2115', '430423000000', '衡山县', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2116', '430424000000', '衡东县', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2117', '430426000000', '祁东县', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2118', '430471000000', '衡阳综合保税区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2119', '430472000000', '湖南衡阳高新技术产业园区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2120', '430473000000', '湖南衡阳松木经济开发区', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2121', '430481000000', '耒阳市', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2122', '430482000000', '常宁市', '3', '430400000000', '2106', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2123', '430500000000', '邵阳市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2124', '430501000000', '市辖区', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2125', '430502000000', '双清区', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2126', '430503000000', '大祥区', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2127', '430511000000', '北塔区', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2128', '430522000000', '新邵县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2129', '430523000000', '邵阳县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2130', '430524000000', '隆回县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2131', '430525000000', '洞口县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2132', '430527000000', '绥宁县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2133', '430528000000', '新宁县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2134', '430529000000', '城步苗族自治县', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2135', '430581000000', '武冈市', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2136', '430582000000', '邵东市', '3', '430500000000', '2123', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2137', '430600000000', '岳阳市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2138', '430601000000', '市辖区', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2139', '430602000000', '岳阳楼区', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2140', '430603000000', '云溪区', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2141', '430611000000', '君山区', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2142', '430621000000', '岳阳县', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2143', '430623000000', '华容县', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2144', '430624000000', '湘阴县', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2145', '430626000000', '平江县', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2146', '430671000000', '岳阳市屈原管理区', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2147', '430681000000', '汨罗市', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2148', '430682000000', '临湘市', '3', '430600000000', '2137', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2149', '430700000000', '常德市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2150', '430701000000', '市辖区', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2151', '430702000000', '武陵区', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2152', '430703000000', '鼎城区', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2153', '430721000000', '安乡县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2154', '430722000000', '汉寿县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2155', '430723000000', '澧县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2156', '430724000000', '临澧县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2157', '430725000000', '桃源县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2158', '430726000000', '石门县', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2159', '430771000000', '常德市西洞庭管理区', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2160', '430781000000', '津市市', '3', '430700000000', '2149', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2161', '430800000000', '张家界市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2162', '430801000000', '市辖区', '3', '430800000000', '2161', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2163', '430802000000', '永定区', '3', '430800000000', '2161', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2164', '430811000000', '武陵源区', '3', '430800000000', '2161', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2165', '430821000000', '慈利县', '3', '430800000000', '2161', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2166', '430822000000', '桑植县', '3', '430800000000', '2161', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2167', '430900000000', '益阳市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2168', '430901000000', '市辖区', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2169', '430902000000', '资阳区', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2170', '430903000000', '赫山区', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2171', '430921000000', '南县', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2172', '430922000000', '桃江县', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2173', '430923000000', '安化县', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2174', '430971000000', '益阳市大通湖管理区', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2175', '430972000000', '湖南益阳高新技术产业园区', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2176', '430981000000', '沅江市', '3', '430900000000', '2167', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2177', '431000000000', '郴州市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2178', '431001000000', '市辖区', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2179', '431002000000', '北湖区', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2180', '431003000000', '苏仙区', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2181', '431021000000', '桂阳县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2182', '431022000000', '宜章县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2183', '431023000000', '永兴县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2184', '431024000000', '嘉禾县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2185', '431025000000', '临武县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2186', '431026000000', '汝城县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2187', '431027000000', '桂东县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2188', '431028000000', '安仁县', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2189', '431081000000', '资兴市', '3', '431000000000', '2177', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2190', '431100000000', '永州市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2191', '431101000000', '市辖区', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2192', '431102000000', '零陵区', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2193', '431103000000', '冷水滩区', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2194', '431122000000', '东安县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2195', '431123000000', '双牌县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2196', '431124000000', '道县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2197', '431125000000', '江永县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2198', '431126000000', '宁远县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2199', '431127000000', '蓝山县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2200', '431128000000', '新田县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2201', '431129000000', '江华瑶族自治县', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2202', '431171000000', '永州经济技术开发区', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2203', '431173000000', '永州市回龙圩管理区', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2204', '431181000000', '祁阳市', '3', '431100000000', '2190', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2205', '431200000000', '怀化市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2206', '431201000000', '市辖区', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2207', '431202000000', '鹤城区', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2208', '431221000000', '中方县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2209', '431222000000', '沅陵县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2210', '431223000000', '辰溪县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2211', '431224000000', '溆浦县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2212', '431225000000', '会同县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2213', '431226000000', '麻阳苗族自治县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2214', '431227000000', '新晃侗族自治县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2215', '431228000000', '芷江侗族自治县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2216', '431229000000', '靖州苗族侗族自治县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2217', '431230000000', '通道侗族自治县', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2218', '431271000000', '怀化市洪江管理区', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2219', '431281000000', '洪江市', '3', '431200000000', '2205', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2220', '431300000000', '娄底市', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2221', '431301000000', '市辖区', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2222', '431302000000', '娄星区', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2223', '431321000000', '双峰县', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2224', '431322000000', '新化县', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2225', '431381000000', '冷水江市', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2226', '431382000000', '涟源市', '3', '431300000000', '2220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2227', '433100000000', '湘西土家族苗族自治州', '2', '430000000000', '2072', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2228', '433101000000', '吉首市', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2229', '433122000000', '泸溪县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2230', '433123000000', '凤凰县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2231', '433124000000', '花垣县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2232', '433125000000', '保靖县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2233', '433126000000', '古丈县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2234', '433127000000', '永顺县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2235', '433130000000', '龙山县', '3', '433100000000', '2227', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2236', '440000000000', '广东省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2237', '440100000000', '广州市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2238', '440101000000', '市辖区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2239', '440103000000', '荔湾区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2240', '440104000000', '越秀区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2241', '440105000000', '海珠区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2242', '440106000000', '天河区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2243', '440111000000', '白云区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2244', '440112000000', '黄埔区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2245', '440113000000', '番禺区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2246', '440114000000', '花都区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2247', '440115000000', '南沙区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2248', '440117000000', '从化区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2249', '440118000000', '增城区', '3', '440100000000', '2237', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2250', '440200000000', '韶关市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2251', '440201000000', '市辖区', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2252', '440203000000', '武江区', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2253', '440204000000', '浈江区', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2254', '440205000000', '曲江区', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2255', '440222000000', '始兴县', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2256', '440224000000', '仁化县', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2257', '440229000000', '翁源县', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2258', '440232000000', '乳源瑶族自治县', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2259', '440233000000', '新丰县', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2260', '440281000000', '乐昌市', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2261', '440282000000', '南雄市', '3', '440200000000', '2250', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2262', '440300000000', '深圳市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2263', '440301000000', '市辖区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2264', '440303000000', '罗湖区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2265', '440304000000', '福田区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2266', '440305000000', '南山区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2267', '440306000000', '宝安区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2268', '440307000000', '龙岗区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2269', '440308000000', '盐田区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2270', '440309000000', '龙华区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2271', '440310000000', '坪山区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2272', '440311000000', '光明区', '3', '440300000000', '2262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2273', '440400000000', '珠海市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2274', '440401000000', '市辖区', '3', '440400000000', '2273', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2275', '440402000000', '香洲区', '3', '440400000000', '2273', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2276', '440403000000', '斗门区', '3', '440400000000', '2273', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2277', '440404000000', '金湾区', '3', '440400000000', '2273', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2278', '440500000000', '汕头市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2279', '440501000000', '市辖区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2280', '440507000000', '龙湖区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2281', '440511000000', '金平区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2282', '440512000000', '濠江区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2283', '440513000000', '潮阳区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2284', '440514000000', '潮南区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2285', '440515000000', '澄海区', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2286', '440523000000', '南澳县', '3', '440500000000', '2278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2287', '440600000000', '佛山市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2288', '440601000000', '市辖区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2289', '440604000000', '禅城区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2290', '440605000000', '南海区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2291', '440606000000', '顺德区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2292', '440607000000', '三水区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2293', '440608000000', '高明区', '3', '440600000000', '2287', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2294', '440700000000', '江门市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2295', '440701000000', '市辖区', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2296', '440703000000', '蓬江区', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2297', '440704000000', '江海区', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2298', '440705000000', '新会区', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2299', '440781000000', '台山市', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2300', '440783000000', '开平市', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2301', '440784000000', '鹤山市', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2302', '440785000000', '恩平市', '3', '440700000000', '2294', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2303', '440800000000', '湛江市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2304', '440801000000', '市辖区', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2305', '440802000000', '赤坎区', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2306', '440803000000', '霞山区', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2307', '440804000000', '坡头区', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2308', '440811000000', '麻章区', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2309', '440823000000', '遂溪县', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2310', '440825000000', '徐闻县', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2311', '440881000000', '廉江市', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2312', '440882000000', '雷州市', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2313', '440883000000', '吴川市', '3', '440800000000', '2303', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2314', '440900000000', '茂名市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2315', '440901000000', '市辖区', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2316', '440902000000', '茂南区', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2317', '440904000000', '电白区', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2318', '440981000000', '高州市', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2319', '440982000000', '化州市', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2320', '440983000000', '信宜市', '3', '440900000000', '2314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2321', '441200000000', '肇庆市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2322', '441201000000', '市辖区', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2323', '441202000000', '端州区', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2324', '441203000000', '鼎湖区', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2325', '441204000000', '高要区', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2326', '441223000000', '广宁县', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2327', '441224000000', '怀集县', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2328', '441225000000', '封开县', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2329', '441226000000', '德庆县', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2330', '441284000000', '四会市', '3', '441200000000', '2321', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2331', '441300000000', '惠州市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2332', '441301000000', '市辖区', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2333', '441302000000', '惠城区', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2334', '441303000000', '惠阳区', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2335', '441322000000', '博罗县', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2336', '441323000000', '惠东县', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2337', '441324000000', '龙门县', '3', '441300000000', '2331', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2338', '441400000000', '梅州市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2339', '441401000000', '市辖区', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2340', '441402000000', '梅江区', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2341', '441403000000', '梅县区', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2342', '441422000000', '大埔县', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2343', '441423000000', '丰顺县', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2344', '441424000000', '五华县', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2345', '441426000000', '平远县', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2346', '441427000000', '蕉岭县', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2347', '441481000000', '兴宁市', '3', '441400000000', '2338', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2348', '441500000000', '汕尾市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2349', '441501000000', '市辖区', '3', '441500000000', '2348', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2350', '441502000000', '城区', '3', '441500000000', '2348', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2351', '441521000000', '海丰县', '3', '441500000000', '2348', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2352', '441523000000', '陆河县', '3', '441500000000', '2348', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2353', '441581000000', '陆丰市', '3', '441500000000', '2348', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2354', '441600000000', '河源市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2355', '441601000000', '市辖区', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2356', '441602000000', '源城区', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2357', '441621000000', '紫金县', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2358', '441622000000', '龙川县', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2359', '441623000000', '连平县', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2360', '441624000000', '和平县', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2361', '441625000000', '东源县', '3', '441600000000', '2354', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2362', '441700000000', '阳江市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2363', '441701000000', '市辖区', '3', '441700000000', '2362', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2364', '441702000000', '江城区', '3', '441700000000', '2362', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2365', '441704000000', '阳东区', '3', '441700000000', '2362', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2366', '441721000000', '阳西县', '3', '441700000000', '2362', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2367', '441781000000', '阳春市', '3', '441700000000', '2362', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2368', '441800000000', '清远市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2369', '441801000000', '市辖区', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2370', '441802000000', '清城区', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2371', '441803000000', '清新区', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2372', '441821000000', '佛冈县', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2373', '441823000000', '阳山县', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2374', '441825000000', '连山壮族瑶族自治县', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2375', '441826000000', '连南瑶族自治县', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2376', '441881000000', '英德市', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2377', '441882000000', '连州市', '3', '441800000000', '2368', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2378', '441900000000', '东莞市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2379', '441900003000', '东城街道', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2380', '441900004000', '南城街道', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2381', '441900005000', '万江街道', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2382', '441900006000', '莞城街道', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2383', '441900101000', '石碣镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2384', '441900102000', '石龙镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2385', '441900103000', '茶山镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2386', '441900104000', '石排镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2387', '441900105000', '企石镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2388', '441900106000', '横沥镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2389', '441900107000', '桥头镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2390', '441900108000', '谢岗镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2391', '441900109000', '东坑镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2392', '441900110000', '常平镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2393', '441900111000', '寮步镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2394', '441900112000', '樟木头镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2395', '441900113000', '大朗镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2396', '441900114000', '黄江镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2397', '441900115000', '清溪镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2398', '441900116000', '塘厦镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2399', '441900117000', '凤岗镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2400', '441900118000', '大岭山镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2401', '441900119000', '长安镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2402', '441900121000', '虎门镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2403', '441900122000', '厚街镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2404', '441900123000', '沙田镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2405', '441900124000', '道滘镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2406', '441900125000', '洪梅镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2407', '441900126000', '麻涌镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2408', '441900127000', '望牛墩镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2409', '441900128000', '中堂镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2410', '441900129000', '高埗镇', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2411', '441900401000', '松山湖', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2412', '441900402000', '东莞港', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2413', '441900403000', '东莞生态园', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2414', '441900404000', '东莞滨海湾新区', '3', '441900000000', '2378', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2415', '442000000000', '中山市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2416', '442000001000', '石岐街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2417', '442000002000', '东区街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2418', '442000003000', '中山港街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2419', '442000004000', '西区街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2420', '442000005000', '南区街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2421', '442000006000', '五桂山街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2422', '442000007000', '民众街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2423', '442000008000', '南朗街道', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2424', '442000101000', '黄圃镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2425', '442000103000', '东凤镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2426', '442000105000', '古镇镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2427', '442000106000', '沙溪镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2428', '442000107000', '坦洲镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2429', '442000108000', '港口镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2430', '442000109000', '三角镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2431', '442000110000', '横栏镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2432', '442000111000', '南头镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2433', '442000112000', '阜沙镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2434', '442000114000', '三乡镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2435', '442000115000', '板芙镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2436', '442000116000', '大涌镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2437', '442000117000', '神湾镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2438', '442000118000', '小榄镇', '3', '442000000000', '2415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2439', '445100000000', '潮州市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2440', '445101000000', '市辖区', '3', '445100000000', '2439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2441', '445102000000', '湘桥区', '3', '445100000000', '2439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2442', '445103000000', '潮安区', '3', '445100000000', '2439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2443', '445122000000', '饶平县', '3', '445100000000', '2439', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2444', '445200000000', '揭阳市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2445', '445201000000', '市辖区', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2446', '445202000000', '榕城区', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2447', '445203000000', '揭东区', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2448', '445222000000', '揭西县', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2449', '445224000000', '惠来县', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2450', '445281000000', '普宁市', '3', '445200000000', '2444', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2451', '445300000000', '云浮市', '2', '440000000000', '2236', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2452', '445301000000', '市辖区', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2453', '445302000000', '云城区', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2454', '445303000000', '云安区', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2455', '445321000000', '新兴县', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2456', '445322000000', '郁南县', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2457', '445381000000', '罗定市', '3', '445300000000', '2451', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2458', '450000000000', '广西壮族自治区', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2459', '450100000000', '南宁市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2460', '450101000000', '市辖区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2461', '450102000000', '兴宁区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2462', '450103000000', '青秀区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2463', '450105000000', '江南区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2464', '450107000000', '西乡塘区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2465', '450108000000', '良庆区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2466', '450109000000', '邕宁区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2467', '450110000000', '武鸣区', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2468', '450123000000', '隆安县', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2469', '450124000000', '马山县', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2470', '450125000000', '上林县', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2471', '450126000000', '宾阳县', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2472', '450181000000', '横州市', '3', '450100000000', '2459', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2473', '450200000000', '柳州市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2474', '450201000000', '市辖区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2475', '450202000000', '城中区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2476', '450203000000', '鱼峰区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2477', '450204000000', '柳南区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2478', '450205000000', '柳北区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2479', '450206000000', '柳江区', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2480', '450222000000', '柳城县', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2481', '450223000000', '鹿寨县', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2482', '450224000000', '融安县', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2483', '450225000000', '融水苗族自治县', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2484', '450226000000', '三江侗族自治县', '3', '450200000000', '2473', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2485', '450300000000', '桂林市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2486', '450301000000', '市辖区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2487', '450302000000', '秀峰区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2488', '450303000000', '叠彩区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2489', '450304000000', '象山区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2490', '450305000000', '七星区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2491', '450311000000', '雁山区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2492', '450312000000', '临桂区', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2493', '450321000000', '阳朔县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2494', '450323000000', '灵川县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2495', '450324000000', '全州县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2496', '450325000000', '兴安县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2497', '450326000000', '永福县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2498', '450327000000', '灌阳县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2499', '450328000000', '龙胜各族自治县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2500', '450329000000', '资源县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2501', '450330000000', '平乐县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2502', '450332000000', '恭城瑶族自治县', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2503', '450381000000', '荔浦市', '3', '450300000000', '2485', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2504', '450400000000', '梧州市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2505', '450401000000', '市辖区', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2506', '450403000000', '万秀区', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2507', '450405000000', '长洲区', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2508', '450406000000', '龙圩区', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2509', '450421000000', '苍梧县', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2510', '450422000000', '藤县', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2511', '450423000000', '蒙山县', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2512', '450481000000', '岑溪市', '3', '450400000000', '2504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2513', '450500000000', '北海市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2514', '450501000000', '市辖区', '3', '450500000000', '2513', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2515', '450502000000', '海城区', '3', '450500000000', '2513', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2516', '450503000000', '银海区', '3', '450500000000', '2513', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2517', '450512000000', '铁山港区', '3', '450500000000', '2513', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2518', '450521000000', '合浦县', '3', '450500000000', '2513', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2519', '450600000000', '防城港市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2520', '450601000000', '市辖区', '3', '450600000000', '2519', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2521', '450602000000', '港口区', '3', '450600000000', '2519', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2522', '450603000000', '防城区', '3', '450600000000', '2519', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2523', '450621000000', '上思县', '3', '450600000000', '2519', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2524', '450681000000', '东兴市', '3', '450600000000', '2519', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2525', '450700000000', '钦州市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2526', '450701000000', '市辖区', '3', '450700000000', '2525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2527', '450702000000', '钦南区', '3', '450700000000', '2525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2528', '450703000000', '钦北区', '3', '450700000000', '2525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2529', '450721000000', '灵山县', '3', '450700000000', '2525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2530', '450722000000', '浦北县', '3', '450700000000', '2525', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2531', '450800000000', '贵港市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2532', '450801000000', '市辖区', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2533', '450802000000', '港北区', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2534', '450803000000', '港南区', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2535', '450804000000', '覃塘区', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2536', '450821000000', '平南县', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2537', '450881000000', '桂平市', '3', '450800000000', '2531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2538', '450900000000', '玉林市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2539', '450901000000', '市辖区', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2540', '450902000000', '玉州区', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2541', '450903000000', '福绵区', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2542', '450921000000', '容县', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2543', '450922000000', '陆川县', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2544', '450923000000', '博白县', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2545', '450924000000', '兴业县', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2546', '450981000000', '北流市', '3', '450900000000', '2538', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2547', '451000000000', '百色市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2548', '451001000000', '市辖区', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2549', '451002000000', '右江区', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2550', '451003000000', '田阳区', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2551', '451022000000', '田东县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2552', '451024000000', '德保县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2553', '451026000000', '那坡县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2554', '451027000000', '凌云县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2555', '451028000000', '乐业县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2556', '451029000000', '田林县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2557', '451030000000', '西林县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2558', '451031000000', '隆林各族自治县', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2559', '451081000000', '靖西市', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2560', '451082000000', '平果市', '3', '451000000000', '2547', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2561', '451100000000', '贺州市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2562', '451101000000', '市辖区', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2563', '451102000000', '八步区', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2564', '451103000000', '平桂区', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2565', '451121000000', '昭平县', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2566', '451122000000', '钟山县', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2567', '451123000000', '富川瑶族自治县', '3', '451100000000', '2561', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2568', '451200000000', '河池市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2569', '451201000000', '市辖区', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2570', '451202000000', '金城江区', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2571', '451203000000', '宜州区', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2572', '451221000000', '南丹县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2573', '451222000000', '天峨县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2574', '451223000000', '凤山县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2575', '451224000000', '东兰县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2576', '451225000000', '罗城仫佬族自治县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2577', '451226000000', '环江毛南族自治县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2578', '451227000000', '巴马瑶族自治县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2579', '451228000000', '都安瑶族自治县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2580', '451229000000', '大化瑶族自治县', '3', '451200000000', '2568', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2581', '451300000000', '来宾市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2582', '451301000000', '市辖区', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2583', '451302000000', '兴宾区', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2584', '451321000000', '忻城县', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2585', '451322000000', '象州县', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2586', '451323000000', '武宣县', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2587', '451324000000', '金秀瑶族自治县', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2588', '451381000000', '合山市', '3', '451300000000', '2581', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2589', '451400000000', '崇左市', '2', '450000000000', '2458', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2590', '451401000000', '市辖区', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2591', '451402000000', '江州区', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2592', '451421000000', '扶绥县', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2593', '451422000000', '宁明县', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2594', '451423000000', '龙州县', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2595', '451424000000', '大新县', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2596', '451425000000', '天等县', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2597', '451481000000', '凭祥市', '3', '451400000000', '2589', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2598', '460000000000', '海南省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2599', '460100000000', '海口市', '2', '460000000000', '2598', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2600', '460101000000', '市辖区', '3', '460100000000', '2599', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2601', '460105000000', '秀英区', '3', '460100000000', '2599', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2602', '460106000000', '龙华区', '3', '460100000000', '2599', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2603', '460107000000', '琼山区', '3', '460100000000', '2599', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2604', '460108000000', '美兰区', '3', '460100000000', '2599', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2605', '460200000000', '三亚市', '2', '460000000000', '2598', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2606', '460201000000', '市辖区', '3', '460200000000', '2605', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2607', '460202000000', '海棠区', '3', '460200000000', '2605', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2608', '460203000000', '吉阳区', '3', '460200000000', '2605', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2609', '460204000000', '天涯区', '3', '460200000000', '2605', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2610', '460205000000', '崖州区', '3', '460200000000', '2605', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2611', '460300000000', '三沙市', '2', '460000000000', '2598', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2612', '460321000000', '西沙群岛', '3', '460300000000', '2611', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2613', '460322000000', '南沙群岛', '3', '460300000000', '2611', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2614', '460323000000', '中沙群岛的岛礁及其海域', '3', '460300000000', '2611', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2615', '460400000000', '儋州市', '2', '460000000000', '2598', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2616', '460400100000', '那大镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2617', '460400101000', '和庆镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2618', '460400102000', '南丰镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2619', '460400103000', '大成镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2620', '460400104000', '雅星镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2621', '460400105000', '兰洋镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2622', '460400106000', '光村镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2623', '460400107000', '木棠镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2624', '460400108000', '海头镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2625', '460400109000', '峨蔓镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2626', '460400111000', '王五镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2627', '460400112000', '白马井镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2628', '460400113000', '中和镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2629', '460400114000', '排浦镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2630', '460400115000', '东成镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2631', '460400116000', '新州镇', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2632', '460400499000', '洋浦经济开发区', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2633', '460400500000', '华南热作学院', '3', '460400000000', '2615', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2634', '469000000000', '省直辖县级行政区划', '2', '460000000000', '2598', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2635', '469001000000', '五指山市', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2636', '469002000000', '琼海市', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2637', '469005000000', '文昌市', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2638', '469006000000', '万宁市', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2639', '469007000000', '东方市', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2640', '469021000000', '定安县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2641', '469022000000', '屯昌县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2642', '469023000000', '澄迈县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2643', '469024000000', '临高县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2644', '469025000000', '白沙黎族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2645', '469026000000', '昌江黎族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2646', '469027000000', '乐东黎族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2647', '469028000000', '陵水黎族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2648', '469029000000', '保亭黎族苗族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2649', '469030000000', '琼中黎族苗族自治县', '3', '469000000000', '2634', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2650', '500000000000', '重庆市', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2651', '500100000000', '市辖区', '2', '500000000000', '2650', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2652', '500101000000', '万州区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2653', '500102000000', '涪陵区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2654', '500103000000', '渝中区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2655', '500104000000', '大渡口区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2656', '500105000000', '江北区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2657', '500106000000', '沙坪坝区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2658', '500107000000', '九龙坡区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2659', '500108000000', '南岸区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2660', '500109000000', '北碚区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2661', '500110000000', '綦江区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2662', '500111000000', '大足区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2663', '500112000000', '渝北区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2664', '500113000000', '巴南区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2665', '500114000000', '黔江区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2666', '500115000000', '长寿区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2667', '500116000000', '江津区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2668', '500117000000', '合川区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2669', '500118000000', '永川区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2670', '500119000000', '南川区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2671', '500120000000', '璧山区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2672', '500151000000', '铜梁区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2673', '500152000000', '潼南区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2674', '500153000000', '荣昌区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2675', '500154000000', '开州区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2676', '500155000000', '梁平区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2677', '500156000000', '武隆区', '3', '500100000000', '2651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2678', '500200000000', '县', '2', '500000000000', '2650', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2679', '500229000000', '城口县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2680', '500230000000', '丰都县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2681', '500231000000', '垫江县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2682', '500233000000', '忠县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2683', '500235000000', '云阳县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2684', '500236000000', '奉节县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2685', '500237000000', '巫山县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2686', '500238000000', '巫溪县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2687', '500240000000', '石柱土家族自治县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2688', '500241000000', '秀山土家族苗族自治县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2689', '500242000000', '酉阳土家族苗族自治县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2690', '500243000000', '彭水苗族土家族自治县', '3', '500200000000', '2678', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2691', '510000000000', '四川省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2692', '510100000000', '成都市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2693', '510101000000', '市辖区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2694', '510104000000', '锦江区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2695', '510105000000', '青羊区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2696', '510106000000', '金牛区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2697', '510107000000', '武侯区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2698', '510108000000', '成华区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2699', '510112000000', '龙泉驿区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2700', '510113000000', '青白江区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2701', '510114000000', '新都区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2702', '510115000000', '温江区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2703', '510116000000', '双流区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2704', '510117000000', '郫都区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2705', '510118000000', '新津区', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2706', '510121000000', '金堂县', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2707', '510129000000', '大邑县', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2708', '510131000000', '蒲江县', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2709', '510181000000', '都江堰市', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2710', '510182000000', '彭州市', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2711', '510183000000', '邛崃市', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2712', '510184000000', '崇州市', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2713', '510185000000', '简阳市', '3', '510100000000', '2692', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2714', '510300000000', '自贡市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2715', '510301000000', '市辖区', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2716', '510302000000', '自流井区', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2717', '510303000000', '贡井区', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2718', '510304000000', '大安区', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2719', '510311000000', '沿滩区', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2720', '510321000000', '荣县', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2721', '510322000000', '富顺县', '3', '510300000000', '2714', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2722', '510400000000', '攀枝花市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2723', '510401000000', '市辖区', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2724', '510402000000', '东区', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2725', '510403000000', '西区', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2726', '510411000000', '仁和区', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2727', '510421000000', '米易县', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2728', '510422000000', '盐边县', '3', '510400000000', '2722', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2729', '510500000000', '泸州市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2730', '510501000000', '市辖区', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2731', '510502000000', '江阳区', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2732', '510503000000', '纳溪区', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2733', '510504000000', '龙马潭区', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2734', '510521000000', '泸县', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2735', '510522000000', '合江县', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2736', '510524000000', '叙永县', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2737', '510525000000', '古蔺县', '3', '510500000000', '2729', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2738', '510600000000', '德阳市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2739', '510601000000', '市辖区', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2740', '510603000000', '旌阳区', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2741', '510604000000', '罗江区', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2742', '510623000000', '中江县', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2743', '510681000000', '广汉市', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2744', '510682000000', '什邡市', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2745', '510683000000', '绵竹市', '3', '510600000000', '2738', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2746', '510700000000', '绵阳市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2747', '510701000000', '市辖区', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2748', '510703000000', '涪城区', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2749', '510704000000', '游仙区', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2750', '510705000000', '安州区', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2751', '510722000000', '三台县', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2752', '510723000000', '盐亭县', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2753', '510725000000', '梓潼县', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2754', '510726000000', '北川羌族自治县', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2755', '510727000000', '平武县', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2756', '510781000000', '江油市', '3', '510700000000', '2746', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2757', '510800000000', '广元市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2758', '510801000000', '市辖区', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2759', '510802000000', '利州区', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2760', '510811000000', '昭化区', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2761', '510812000000', '朝天区', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2762', '510821000000', '旺苍县', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2763', '510822000000', '青川县', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2764', '510823000000', '剑阁县', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2765', '510824000000', '苍溪县', '3', '510800000000', '2757', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2766', '510900000000', '遂宁市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2767', '510901000000', '市辖区', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2768', '510903000000', '船山区', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2769', '510904000000', '安居区', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2770', '510921000000', '蓬溪县', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2771', '510923000000', '大英县', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2772', '510981000000', '射洪市', '3', '510900000000', '2766', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2773', '511000000000', '内江市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2774', '511001000000', '市辖区', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2775', '511002000000', '市中区', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2776', '511011000000', '东兴区', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2777', '511024000000', '威远县', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2778', '511025000000', '资中县', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2779', '511071000000', '内江经济开发区', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2780', '511083000000', '隆昌市', '3', '511000000000', '2773', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2781', '511100000000', '乐山市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2782', '511101000000', '市辖区', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2783', '511102000000', '市中区', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2784', '511111000000', '沙湾区', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2785', '511112000000', '五通桥区', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2786', '511113000000', '金口河区', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2787', '511123000000', '犍为县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2788', '511124000000', '井研县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2789', '511126000000', '夹江县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2790', '511129000000', '沐川县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2791', '511132000000', '峨边彝族自治县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2792', '511133000000', '马边彝族自治县', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2793', '511181000000', '峨眉山市', '3', '511100000000', '2781', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2794', '511300000000', '南充市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2795', '511301000000', '市辖区', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2796', '511302000000', '顺庆区', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2797', '511303000000', '高坪区', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2798', '511304000000', '嘉陵区', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2799', '511321000000', '南部县', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2800', '511322000000', '营山县', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2801', '511323000000', '蓬安县', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2802', '511324000000', '仪陇县', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2803', '511325000000', '西充县', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2804', '511381000000', '阆中市', '3', '511300000000', '2794', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2805', '511400000000', '眉山市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2806', '511401000000', '市辖区', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2807', '511402000000', '东坡区', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2808', '511403000000', '彭山区', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2809', '511421000000', '仁寿县', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2810', '511423000000', '洪雅县', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2811', '511424000000', '丹棱县', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2812', '511425000000', '青神县', '3', '511400000000', '2805', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2813', '511500000000', '宜宾市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2814', '511501000000', '市辖区', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2815', '511502000000', '翠屏区', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2816', '511503000000', '南溪区', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2817', '511504000000', '叙州区', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2818', '511523000000', '江安县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2819', '511524000000', '长宁县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2820', '511525000000', '高县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2821', '511526000000', '珙县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2822', '511527000000', '筠连县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2823', '511528000000', '兴文县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2824', '511529000000', '屏山县', '3', '511500000000', '2813', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2825', '511600000000', '广安市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2826', '511601000000', '市辖区', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2827', '511602000000', '广安区', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2828', '511603000000', '前锋区', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2829', '511621000000', '岳池县', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2830', '511622000000', '武胜县', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2831', '511623000000', '邻水县', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2832', '511681000000', '华蓥市', '3', '511600000000', '2825', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2833', '511700000000', '达州市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2834', '511701000000', '市辖区', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2835', '511702000000', '通川区', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2836', '511703000000', '达川区', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2837', '511722000000', '宣汉县', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2838', '511723000000', '开江县', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2839', '511724000000', '大竹县', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2840', '511725000000', '渠县', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2841', '511771000000', '达州经济开发区', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2842', '511781000000', '万源市', '3', '511700000000', '2833', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2843', '511800000000', '雅安市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2844', '511801000000', '市辖区', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2845', '511802000000', '雨城区', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2846', '511803000000', '名山区', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2847', '511822000000', '荥经县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2848', '511823000000', '汉源县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2849', '511824000000', '石棉县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2850', '511825000000', '天全县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2851', '511826000000', '芦山县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2852', '511827000000', '宝兴县', '3', '511800000000', '2843', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2853', '511900000000', '巴中市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2854', '511901000000', '市辖区', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2855', '511902000000', '巴州区', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2856', '511903000000', '恩阳区', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2857', '511921000000', '通江县', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2858', '511922000000', '南江县', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2859', '511923000000', '平昌县', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2860', '511971000000', '巴中经济开发区', '3', '511900000000', '2853', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2861', '512000000000', '资阳市', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2862', '512001000000', '市辖区', '3', '512000000000', '2861', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2863', '512002000000', '雁江区', '3', '512000000000', '2861', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2864', '512021000000', '安岳县', '3', '512000000000', '2861', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2865', '512022000000', '乐至县', '3', '512000000000', '2861', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2866', '513200000000', '阿坝藏族羌族自治州', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2867', '513201000000', '马尔康市', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2868', '513221000000', '汶川县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2869', '513222000000', '理县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2870', '513223000000', '茂县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2871', '513224000000', '松潘县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2872', '513225000000', '九寨沟县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2873', '513226000000', '金川县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2874', '513227000000', '小金县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2875', '513228000000', '黑水县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2876', '513230000000', '壤塘县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2877', '513231000000', '阿坝县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2878', '513232000000', '若尔盖县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2879', '513233000000', '红原县', '3', '513200000000', '2866', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2880', '513300000000', '甘孜藏族自治州', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2881', '513301000000', '康定市', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2882', '513322000000', '泸定县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2883', '513323000000', '丹巴县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2884', '513324000000', '九龙县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2885', '513325000000', '雅江县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2886', '513326000000', '道孚县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2887', '513327000000', '炉霍县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2888', '513328000000', '甘孜县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2889', '513329000000', '新龙县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2890', '513330000000', '德格县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2891', '513331000000', '白玉县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2892', '513332000000', '石渠县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2893', '513333000000', '色达县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2894', '513334000000', '理塘县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2895', '513335000000', '巴塘县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2896', '513336000000', '乡城县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2897', '513337000000', '稻城县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2898', '513338000000', '得荣县', '3', '513300000000', '2880', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2899', '513400000000', '凉山彝族自治州', '2', '510000000000', '2691', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2900', '513401000000', '西昌市', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2901', '513402000000', '会理市', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2902', '513422000000', '木里藏族自治县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2903', '513423000000', '盐源县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2904', '513424000000', '德昌县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2905', '513426000000', '会东县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2906', '513427000000', '宁南县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2907', '513428000000', '普格县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2908', '513429000000', '布拖县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2909', '513430000000', '金阳县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2910', '513431000000', '昭觉县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2911', '513432000000', '喜德县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2912', '513433000000', '冕宁县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2913', '513434000000', '越西县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2914', '513435000000', '甘洛县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2915', '513436000000', '美姑县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2916', '513437000000', '雷波县', '3', '513400000000', '2899', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2917', '520000000000', '贵州省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2918', '520100000000', '贵阳市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2919', '520101000000', '市辖区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2920', '520102000000', '南明区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2921', '520103000000', '云岩区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2922', '520111000000', '花溪区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2923', '520112000000', '乌当区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2924', '520113000000', '白云区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2925', '520115000000', '观山湖区', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2926', '520121000000', '开阳县', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2927', '520122000000', '息烽县', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2928', '520123000000', '修文县', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2929', '520181000000', '清镇市', '3', '520100000000', '2918', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2930', '520200000000', '六盘水市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2931', '520201000000', '钟山区', '3', '520200000000', '2930', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2932', '520203000000', '六枝特区', '3', '520200000000', '2930', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2933', '520204000000', '水城区', '3', '520200000000', '2930', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2934', '520281000000', '盘州市', '3', '520200000000', '2930', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2935', '520300000000', '遵义市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2936', '520301000000', '市辖区', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2937', '520302000000', '红花岗区', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2938', '520303000000', '汇川区', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2939', '520304000000', '播州区', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2940', '520322000000', '桐梓县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2941', '520323000000', '绥阳县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2942', '520324000000', '正安县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2943', '520325000000', '道真仡佬族苗族自治县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2944', '520326000000', '务川仡佬族苗族自治县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2945', '520327000000', '凤冈县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2946', '520328000000', '湄潭县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2947', '520329000000', '余庆县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2948', '520330000000', '习水县', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2949', '520381000000', '赤水市', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2950', '520382000000', '仁怀市', '3', '520300000000', '2935', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2951', '520400000000', '安顺市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2952', '520401000000', '市辖区', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2953', '520402000000', '西秀区', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2954', '520403000000', '平坝区', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2955', '520422000000', '普定县', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2956', '520423000000', '镇宁布依族苗族自治县', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2957', '520424000000', '关岭布依族苗族自治县', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2958', '520425000000', '紫云苗族布依族自治县', '3', '520400000000', '2951', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2959', '520500000000', '毕节市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2960', '520501000000', '市辖区', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2961', '520502000000', '七星关区', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2962', '520521000000', '大方县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2963', '520523000000', '金沙县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2964', '520524000000', '织金县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2965', '520525000000', '纳雍县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2966', '520526000000', '威宁彝族回族苗族自治县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2967', '520527000000', '赫章县', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2968', '520581000000', '黔西市', '3', '520500000000', '2959', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2969', '520600000000', '铜仁市', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2970', '520601000000', '市辖区', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2971', '520602000000', '碧江区', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2972', '520603000000', '万山区', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2973', '520621000000', '江口县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2974', '520622000000', '玉屏侗族自治县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2975', '520623000000', '石阡县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2976', '520624000000', '思南县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2977', '520625000000', '印江土家族苗族自治县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2978', '520626000000', '德江县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2979', '520627000000', '沿河土家族自治县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2980', '520628000000', '松桃苗族自治县', '3', '520600000000', '2969', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2981', '522300000000', '黔西南布依族苗族自治州', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2982', '522301000000', '兴义市', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2983', '522302000000', '兴仁市', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2984', '522323000000', '普安县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2985', '522324000000', '晴隆县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2986', '522325000000', '贞丰县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2987', '522326000000', '望谟县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2988', '522327000000', '册亨县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2989', '522328000000', '安龙县', '3', '522300000000', '2981', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2990', '522600000000', '黔东南苗族侗族自治州', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('2991', '522601000000', '凯里市', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2992', '522622000000', '黄平县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2993', '522623000000', '施秉县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2994', '522624000000', '三穗县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2995', '522625000000', '镇远县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2996', '522626000000', '岑巩县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2997', '522627000000', '天柱县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2998', '522628000000', '锦屏县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('2999', '522629000000', '剑河县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3000', '522630000000', '台江县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3001', '522631000000', '黎平县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3002', '522632000000', '榕江县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3003', '522633000000', '从江县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3004', '522634000000', '雷山县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3005', '522635000000', '麻江县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3006', '522636000000', '丹寨县', '3', '522600000000', '2990', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3007', '522700000000', '黔南布依族苗族自治州', '2', '520000000000', '2917', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3008', '522701000000', '都匀市', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3009', '522702000000', '福泉市', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3010', '522722000000', '荔波县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3011', '522723000000', '贵定县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3012', '522725000000', '瓮安县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3013', '522726000000', '独山县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3014', '522727000000', '平塘县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3015', '522728000000', '罗甸县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3016', '522729000000', '长顺县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3017', '522730000000', '龙里县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3018', '522731000000', '惠水县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3019', '522732000000', '三都水族自治县', '3', '522700000000', '3007', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3020', '530000000000', '云南省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3021', '530100000000', '昆明市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3022', '530101000000', '市辖区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3023', '530102000000', '五华区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3024', '530103000000', '盘龙区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3025', '530111000000', '官渡区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3026', '530112000000', '西山区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3027', '530113000000', '东川区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3028', '530114000000', '呈贡区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3029', '530115000000', '晋宁区', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3030', '530124000000', '富民县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3031', '530125000000', '宜良县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3032', '530126000000', '石林彝族自治县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3033', '530127000000', '嵩明县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3034', '530128000000', '禄劝彝族苗族自治县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3035', '530129000000', '寻甸回族彝族自治县', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3036', '530181000000', '安宁市', '3', '530100000000', '3021', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3037', '530300000000', '曲靖市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3038', '530301000000', '市辖区', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3039', '530302000000', '麒麟区', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3040', '530303000000', '沾益区', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3041', '530304000000', '马龙区', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3042', '530322000000', '陆良县', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3043', '530323000000', '师宗县', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3044', '530324000000', '罗平县', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3045', '530325000000', '富源县', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3046', '530326000000', '会泽县', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3047', '530381000000', '宣威市', '3', '530300000000', '3037', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3048', '530400000000', '玉溪市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3049', '530401000000', '市辖区', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3050', '530402000000', '红塔区', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3051', '530403000000', '江川区', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3052', '530423000000', '通海县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3053', '530424000000', '华宁县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3054', '530425000000', '易门县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3055', '530426000000', '峨山彝族自治县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3056', '530427000000', '新平彝族傣族自治县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3057', '530428000000', '元江哈尼族彝族傣族自治县', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3058', '530481000000', '澄江市', '3', '530400000000', '3048', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3059', '530500000000', '保山市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3060', '530501000000', '市辖区', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3061', '530502000000', '隆阳区', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3062', '530521000000', '施甸县', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3063', '530523000000', '龙陵县', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3064', '530524000000', '昌宁县', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3065', '530581000000', '腾冲市', '3', '530500000000', '3059', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3066', '530600000000', '昭通市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3067', '530601000000', '市辖区', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3068', '530602000000', '昭阳区', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3069', '530621000000', '鲁甸县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3070', '530622000000', '巧家县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3071', '530623000000', '盐津县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3072', '530624000000', '大关县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3073', '530625000000', '永善县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3074', '530626000000', '绥江县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3075', '530627000000', '镇雄县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3076', '530628000000', '彝良县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3077', '530629000000', '威信县', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3078', '530681000000', '水富市', '3', '530600000000', '3066', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3079', '530700000000', '丽江市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3080', '530701000000', '市辖区', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3081', '530702000000', '古城区', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3082', '530721000000', '玉龙纳西族自治县', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3083', '530722000000', '永胜县', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3084', '530723000000', '华坪县', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3085', '530724000000', '宁蒗彝族自治县', '3', '530700000000', '3079', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3086', '530800000000', '普洱市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3087', '530801000000', '市辖区', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3088', '530802000000', '思茅区', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3089', '530821000000', '宁洱哈尼族彝族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3090', '530822000000', '墨江哈尼族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3091', '530823000000', '景东彝族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3092', '530824000000', '景谷傣族彝族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3093', '530825000000', '镇沅彝族哈尼族拉祜族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('3094', '530826000000', '江城哈尼族彝族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3095', '530827000000', '孟连傣族拉祜族佤族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3096', '530828000000', '澜沧拉祜族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3097', '530829000000', '西盟佤族自治县', '3', '530800000000', '3086', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3098', '530900000000', '临沧市', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3099', '530901000000', '市辖区', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3100', '530902000000', '临翔区', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3101', '530921000000', '凤庆县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3102', '530922000000', '云县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3103', '530923000000', '永德县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3104', '530924000000', '镇康县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3105', '530925000000', '双江拉祜族佤族布朗族傣族自治县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('3106', '530926000000', '耿马傣族佤族自治县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3107', '530927000000', '沧源佤族自治县', '3', '530900000000', '3098', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3108', '532300000000', '楚雄彝族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3109', '532301000000', '楚雄市', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3110', '532302000000', '禄丰市', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3111', '532322000000', '双柏县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3112', '532323000000', '牟定县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3113', '532324000000', '南华县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3114', '532325000000', '姚安县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3115', '532326000000', '大姚县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3116', '532327000000', '永仁县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3117', '532328000000', '元谋县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3118', '532329000000', '武定县', '3', '532300000000', '3108', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3119', '532500000000', '红河哈尼族彝族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3120', '532501000000', '个旧市', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3121', '532502000000', '开远市', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3122', '532503000000', '蒙自市', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3123', '532504000000', '弥勒市', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3124', '532523000000', '屏边苗族自治县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3125', '532524000000', '建水县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3126', '532525000000', '石屏县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3127', '532527000000', '泸西县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3128', '532528000000', '元阳县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3129', '532529000000', '红河县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3130', '532530000000', '金平苗族瑶族傣族自治县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3131', '532531000000', '绿春县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3132', '532532000000', '河口瑶族自治县', '3', '532500000000', '3119', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3133', '532600000000', '文山壮族苗族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3134', '532601000000', '文山市', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3135', '532622000000', '砚山县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3136', '532623000000', '西畴县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3137', '532624000000', '麻栗坡县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3138', '532625000000', '马关县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3139', '532626000000', '丘北县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3140', '532627000000', '广南县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3141', '532628000000', '富宁县', '3', '532600000000', '3133', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3142', '532800000000', '西双版纳傣族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3143', '532801000000', '景洪市', '3', '532800000000', '3142', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3144', '532822000000', '勐海县', '3', '532800000000', '3142', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3145', '532823000000', '勐腊县', '3', '532800000000', '3142', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3146', '532900000000', '大理白族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3147', '532901000000', '大理市', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3148', '532922000000', '漾濞彝族自治县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3149', '532923000000', '祥云县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3150', '532924000000', '宾川县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3151', '532925000000', '弥渡县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3152', '532926000000', '南涧彝族自治县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3153', '532927000000', '巍山彝族回族自治县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3154', '532928000000', '永平县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3155', '532929000000', '云龙县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3156', '532930000000', '洱源县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3157', '532931000000', '剑川县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3158', '532932000000', '鹤庆县', '3', '532900000000', '3146', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3159', '533100000000', '德宏傣族景颇族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3160', '533102000000', '瑞丽市', '3', '533100000000', '3159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3161', '533103000000', '芒市', '3', '533100000000', '3159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3162', '533122000000', '梁河县', '3', '533100000000', '3159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3163', '533123000000', '盈江县', '3', '533100000000', '3159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3164', '533124000000', '陇川县', '3', '533100000000', '3159', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3165', '533300000000', '怒江傈僳族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3166', '533301000000', '泸水市', '3', '533300000000', '3165', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3167', '533323000000', '福贡县', '3', '533300000000', '3165', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3168', '533324000000', '贡山独龙族怒族自治县', '3', '533300000000', '3165', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3169', '533325000000', '兰坪白族普米族自治县', '3', '533300000000', '3165', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3170', '533400000000', '迪庆藏族自治州', '2', '530000000000', '3020', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3171', '533401000000', '香格里拉市', '3', '533400000000', '3170', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3172', '533422000000', '德钦县', '3', '533400000000', '3170', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3173', '533423000000', '维西傈僳族自治县', '3', '533400000000', '3170', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3174', '540000000000', '西藏自治区', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3175', '540100000000', '拉萨市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3176', '540101000000', '市辖区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3177', '540102000000', '城关区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3178', '540103000000', '堆龙德庆区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3179', '540104000000', '达孜区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3180', '540121000000', '林周县', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3181', '540122000000', '当雄县', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3182', '540123000000', '尼木县', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3183', '540124000000', '曲水县', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3184', '540127000000', '墨竹工卡县', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3185', '540171000000', '格尔木藏青工业园区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3186', '540172000000', '拉萨经济技术开发区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3187', '540173000000', '西藏文化旅游创意园区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3188', '540174000000', '达孜工业园区', '3', '540100000000', '3175', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3189', '540200000000', '日喀则市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3190', '540202000000', '桑珠孜区', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3191', '540221000000', '南木林县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3192', '540222000000', '江孜县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3193', '540223000000', '定日县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3194', '540224000000', '萨迦县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3195', '540225000000', '拉孜县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3196', '540226000000', '昂仁县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3197', '540227000000', '谢通门县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3198', '540228000000', '白朗县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3199', '540229000000', '仁布县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3200', '540230000000', '康马县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3201', '540231000000', '定结县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3202', '540232000000', '仲巴县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3203', '540233000000', '亚东县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3204', '540234000000', '吉隆县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3205', '540235000000', '聂拉木县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3206', '540236000000', '萨嘎县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3207', '540237000000', '岗巴县', '3', '540200000000', '3189', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3208', '540300000000', '昌都市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3209', '540302000000', '卡若区', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3210', '540321000000', '江达县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3211', '540322000000', '贡觉县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3212', '540323000000', '类乌齐县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3213', '540324000000', '丁青县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3214', '540325000000', '察雅县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3215', '540326000000', '八宿县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3216', '540327000000', '左贡县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3217', '540328000000', '芒康县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3218', '540329000000', '洛隆县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3219', '540330000000', '边坝县', '3', '540300000000', '3208', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3220', '540400000000', '林芝市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3221', '540402000000', '巴宜区', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3222', '540421000000', '工布江达县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3223', '540422000000', '米林县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3224', '540423000000', '墨脱县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3225', '540424000000', '波密县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3226', '540425000000', '察隅县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3227', '540426000000', '朗县', '3', '540400000000', '3220', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3228', '540500000000', '山南市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3229', '540501000000', '市辖区', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3230', '540502000000', '乃东区', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3231', '540521000000', '扎囊县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3232', '540522000000', '贡嘎县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3233', '540523000000', '桑日县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3234', '540524000000', '琼结县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3235', '540525000000', '曲松县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3236', '540526000000', '措美县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3237', '540527000000', '洛扎县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3238', '540528000000', '加查县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3239', '540529000000', '隆子县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3240', '540530000000', '错那县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3241', '540531000000', '浪卡子县', '3', '540500000000', '3228', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3242', '540600000000', '那曲市', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3243', '540602000000', '色尼区', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3244', '540621000000', '嘉黎县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3245', '540622000000', '比如县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3246', '540623000000', '聂荣县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3247', '540624000000', '安多县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3248', '540625000000', '申扎县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3249', '540626000000', '索县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3250', '540627000000', '班戈县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3251', '540628000000', '巴青县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3252', '540629000000', '尼玛县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3253', '540630000000', '双湖县', '3', '540600000000', '3242', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3254', '542500000000', '阿里地区', '2', '540000000000', '3174', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3255', '542521000000', '普兰县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3256', '542522000000', '札达县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3257', '542523000000', '噶尔县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3258', '542524000000', '日土县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3259', '542525000000', '革吉县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3260', '542526000000', '改则县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3261', '542527000000', '措勤县', '3', '542500000000', '3254', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3262', '610000000000', '陕西省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3263', '610100000000', '西安市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3264', '610101000000', '市辖区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3265', '610102000000', '新城区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3266', '610103000000', '碑林区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3267', '610104000000', '莲湖区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3268', '610111000000', '灞桥区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3269', '610112000000', '未央区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3270', '610113000000', '雁塔区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3271', '610114000000', '阎良区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3272', '610115000000', '临潼区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3273', '610116000000', '长安区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3274', '610117000000', '高陵区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3275', '610118000000', '鄠邑区', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3276', '610122000000', '蓝田县', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3277', '610124000000', '周至县', '3', '610100000000', '3263', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3278', '610200000000', '铜川市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3279', '610201000000', '市辖区', '3', '610200000000', '3278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3280', '610202000000', '王益区', '3', '610200000000', '3278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3281', '610203000000', '印台区', '3', '610200000000', '3278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3282', '610204000000', '耀州区', '3', '610200000000', '3278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3283', '610222000000', '宜君县', '3', '610200000000', '3278', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3284', '610300000000', '宝鸡市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3285', '610301000000', '市辖区', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3286', '610302000000', '渭滨区', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3287', '610303000000', '金台区', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3288', '610304000000', '陈仓区', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3289', '610305000000', '凤翔区', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3290', '610323000000', '岐山县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3291', '610324000000', '扶风县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3292', '610326000000', '眉县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3293', '610327000000', '陇县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3294', '610328000000', '千阳县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3295', '610329000000', '麟游县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3296', '610330000000', '凤县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3297', '610331000000', '太白县', '3', '610300000000', '3284', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3298', '610400000000', '咸阳市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3299', '610401000000', '市辖区', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3300', '610402000000', '秦都区', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3301', '610403000000', '杨陵区', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3302', '610404000000', '渭城区', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3303', '610422000000', '三原县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3304', '610423000000', '泾阳县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3305', '610424000000', '乾县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3306', '610425000000', '礼泉县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3307', '610426000000', '永寿县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3308', '610428000000', '长武县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3309', '610429000000', '旬邑县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3310', '610430000000', '淳化县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3311', '610431000000', '武功县', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3312', '610481000000', '兴平市', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3313', '610482000000', '彬州市', '3', '610400000000', '3298', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3314', '610500000000', '渭南市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3315', '610501000000', '市辖区', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3316', '610502000000', '临渭区', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3317', '610503000000', '华州区', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3318', '610522000000', '潼关县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3319', '610523000000', '大荔县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3320', '610524000000', '合阳县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3321', '610525000000', '澄城县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3322', '610526000000', '蒲城县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3323', '610527000000', '白水县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3324', '610528000000', '富平县', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3325', '610581000000', '韩城市', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3326', '610582000000', '华阴市', '3', '610500000000', '3314', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3327', '610600000000', '延安市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3328', '610601000000', '市辖区', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3329', '610602000000', '宝塔区', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3330', '610603000000', '安塞区', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3331', '610621000000', '延长县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3332', '610622000000', '延川县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3333', '610625000000', '志丹县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3334', '610626000000', '吴起县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3335', '610627000000', '甘泉县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3336', '610628000000', '富县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3337', '610629000000', '洛川县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3338', '610630000000', '宜川县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3339', '610631000000', '黄龙县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3340', '610632000000', '黄陵县', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3341', '610681000000', '子长市', '3', '610600000000', '3327', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3342', '610700000000', '汉中市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3343', '610701000000', '市辖区', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3344', '610702000000', '汉台区', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3345', '610703000000', '南郑区', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3346', '610722000000', '城固县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3347', '610723000000', '洋县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3348', '610724000000', '西乡县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3349', '610725000000', '勉县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3350', '610726000000', '宁强县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3351', '610727000000', '略阳县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3352', '610728000000', '镇巴县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3353', '610729000000', '留坝县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3354', '610730000000', '佛坪县', '3', '610700000000', '3342', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3355', '610800000000', '榆林市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3356', '610801000000', '市辖区', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3357', '610802000000', '榆阳区', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3358', '610803000000', '横山区', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3359', '610822000000', '府谷县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3360', '610824000000', '靖边县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3361', '610825000000', '定边县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3362', '610826000000', '绥德县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3363', '610827000000', '米脂县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3364', '610828000000', '佳县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3365', '610829000000', '吴堡县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3366', '610830000000', '清涧县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3367', '610831000000', '子洲县', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3368', '610881000000', '神木市', '3', '610800000000', '3355', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3369', '610900000000', '安康市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3370', '610901000000', '市辖区', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3371', '610902000000', '汉滨区', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3372', '610921000000', '汉阴县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3373', '610922000000', '石泉县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3374', '610923000000', '宁陕县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3375', '610924000000', '紫阳县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3376', '610925000000', '岚皋县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3377', '610926000000', '平利县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3378', '610927000000', '镇坪县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3379', '610929000000', '白河县', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3380', '610981000000', '旬阳市', '3', '610900000000', '3369', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3381', '611000000000', '商洛市', '2', '610000000000', '3262', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3382', '611001000000', '市辖区', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3383', '611002000000', '商州区', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3384', '611021000000', '洛南县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3385', '611022000000', '丹凤县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3386', '611023000000', '商南县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3387', '611024000000', '山阳县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3388', '611025000000', '镇安县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3389', '611026000000', '柞水县', '3', '611000000000', '3381', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3390', '620000000000', '甘肃省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3391', '620100000000', '兰州市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3392', '620101000000', '市辖区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3393', '620102000000', '城关区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3394', '620103000000', '七里河区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3395', '620104000000', '西固区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3396', '620105000000', '安宁区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3397', '620111000000', '红古区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3398', '620121000000', '永登县', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3399', '620122000000', '皋兰县', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3400', '620123000000', '榆中县', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3401', '620171000000', '兰州新区', '3', '620100000000', '3391', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3402', '620200000000', '嘉峪关市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3403', '620201000000', '市辖区', '3', '620200000000', '3402', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3404', '620300000000', '金昌市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3405', '620301000000', '市辖区', '3', '620300000000', '3404', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3406', '620302000000', '金川区', '3', '620300000000', '3404', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3407', '620321000000', '永昌县', '3', '620300000000', '3404', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3408', '620400000000', '白银市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3409', '620401000000', '市辖区', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3410', '620402000000', '白银区', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3411', '620403000000', '平川区', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3412', '620421000000', '靖远县', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3413', '620422000000', '会宁县', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3414', '620423000000', '景泰县', '3', '620400000000', '3408', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3415', '620500000000', '天水市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3416', '620501000000', '市辖区', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3417', '620502000000', '秦州区', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3418', '620503000000', '麦积区', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3419', '620521000000', '清水县', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3420', '620522000000', '秦安县', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3421', '620523000000', '甘谷县', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3422', '620524000000', '武山县', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3423', '620525000000', '张家川回族自治县', '3', '620500000000', '3415', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3424', '620600000000', '武威市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3425', '620601000000', '市辖区', '3', '620600000000', '3424', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3426', '620602000000', '凉州区', '3', '620600000000', '3424', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3427', '620621000000', '民勤县', '3', '620600000000', '3424', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3428', '620622000000', '古浪县', '3', '620600000000', '3424', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3429', '620623000000', '天祝藏族自治县', '3', '620600000000', '3424', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3430', '620700000000', '张掖市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3431', '620701000000', '市辖区', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3432', '620702000000', '甘州区', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3433', '620721000000', '肃南裕固族自治县', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3434', '620722000000', '民乐县', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3435', '620723000000', '临泽县', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3436', '620724000000', '高台县', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3437', '620725000000', '山丹县', '3', '620700000000', '3430', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3438', '620800000000', '平凉市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3439', '620801000000', '市辖区', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3440', '620802000000', '崆峒区', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3441', '620821000000', '泾川县', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3442', '620822000000', '灵台县', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3443', '620823000000', '崇信县', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3444', '620825000000', '庄浪县', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3445', '620826000000', '静宁县', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3446', '620881000000', '华亭市', '3', '620800000000', '3438', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3447', '620900000000', '酒泉市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3448', '620901000000', '市辖区', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3449', '620902000000', '肃州区', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3450', '620921000000', '金塔县', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3451', '620922000000', '瓜州县', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3452', '620923000000', '肃北蒙古族自治县', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3453', '620924000000', '阿克塞哈萨克族自治县', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3454', '620981000000', '玉门市', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3455', '620982000000', '敦煌市', '3', '620900000000', '3447', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3456', '621000000000', '庆阳市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3457', '621001000000', '市辖区', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3458', '621002000000', '西峰区', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3459', '621021000000', '庆城县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3460', '621022000000', '环县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3461', '621023000000', '华池县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3462', '621024000000', '合水县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3463', '621025000000', '正宁县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3464', '621026000000', '宁县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3465', '621027000000', '镇原县', '3', '621000000000', '3456', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3466', '621100000000', '定西市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3467', '621101000000', '市辖区', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3468', '621102000000', '安定区', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3469', '621121000000', '通渭县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3470', '621122000000', '陇西县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3471', '621123000000', '渭源县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3472', '621124000000', '临洮县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3473', '621125000000', '漳县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3474', '621126000000', '岷县', '3', '621100000000', '3466', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3475', '621200000000', '陇南市', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3476', '621201000000', '市辖区', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3477', '621202000000', '武都区', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3478', '621221000000', '成县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3479', '621222000000', '文县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3480', '621223000000', '宕昌县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3481', '621224000000', '康县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3482', '621225000000', '西和县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3483', '621226000000', '礼县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3484', '621227000000', '徽县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3485', '621228000000', '两当县', '3', '621200000000', '3475', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3486', '622900000000', '临夏回族自治州', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3487', '622901000000', '临夏市', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3488', '622921000000', '临夏县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3489', '622922000000', '康乐县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3490', '622923000000', '永靖县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3491', '622924000000', '广河县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3492', '622925000000', '和政县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3493', '622926000000', '东乡族自治县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3494', '622927000000', '积石山保安族东乡族撒拉族自治县', '3', '622900000000', '3486', '1', '2022-01-21 13:15:57', null, '0',
        '0', '1');
INSERT INTO `administrative_area`
VALUES ('3495', '623000000000', '甘南藏族自治州', '2', '620000000000', '3390', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3496', '623001000000', '合作市', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3497', '623021000000', '临潭县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3498', '623022000000', '卓尼县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3499', '623023000000', '舟曲县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3500', '623024000000', '迭部县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3501', '623025000000', '玛曲县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3502', '623026000000', '碌曲县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3503', '623027000000', '夏河县', '3', '623000000000', '3495', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3504', '630000000000', '青海省', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3505', '630100000000', '西宁市', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3506', '630101000000', '市辖区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3507', '630102000000', '城东区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3508', '630103000000', '城中区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3509', '630104000000', '城西区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3510', '630105000000', '城北区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3511', '630106000000', '湟中区', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3512', '630121000000', '大通回族土族自治县', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3513', '630123000000', '湟源县', '3', '630100000000', '3505', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3514', '630200000000', '海东市', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3515', '630202000000', '乐都区', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3516', '630203000000', '平安区', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3517', '630222000000', '民和回族土族自治县', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3518', '630223000000', '互助土族自治县', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3519', '630224000000', '化隆回族自治县', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3520', '630225000000', '循化撒拉族自治县', '3', '630200000000', '3514', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3521', '632200000000', '海北藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3522', '632221000000', '门源回族自治县', '3', '632200000000', '3521', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3523', '632222000000', '祁连县', '3', '632200000000', '3521', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3524', '632223000000', '海晏县', '3', '632200000000', '3521', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3525', '632224000000', '刚察县', '3', '632200000000', '3521', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3526', '632300000000', '黄南藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3527', '632301000000', '同仁市', '3', '632300000000', '3526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3528', '632322000000', '尖扎县', '3', '632300000000', '3526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3529', '632323000000', '泽库县', '3', '632300000000', '3526', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3530', '632324000000', '河南蒙古族自治县', '3', '632300000000', '3526', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3531', '632500000000', '海南藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3532', '632521000000', '共和县', '3', '632500000000', '3531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3533', '632522000000', '同德县', '3', '632500000000', '3531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3534', '632523000000', '贵德县', '3', '632500000000', '3531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3535', '632524000000', '兴海县', '3', '632500000000', '3531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3536', '632525000000', '贵南县', '3', '632500000000', '3531', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3537', '632600000000', '果洛藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3538', '632621000000', '玛沁县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3539', '632622000000', '班玛县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3540', '632623000000', '甘德县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3541', '632624000000', '达日县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3542', '632625000000', '久治县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3543', '632626000000', '玛多县', '3', '632600000000', '3537', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3544', '632700000000', '玉树藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3545', '632701000000', '玉树市', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3546', '632722000000', '杂多县', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3547', '632723000000', '称多县', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3548', '632724000000', '治多县', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3549', '632725000000', '囊谦县', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3550', '632726000000', '曲麻莱县', '3', '632700000000', '3544', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3551', '632800000000', '海西蒙古族藏族自治州', '2', '630000000000', '3504', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3552', '632801000000', '格尔木市', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3553', '632802000000', '德令哈市', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3554', '632803000000', '茫崖市', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3555', '632821000000', '乌兰县', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3556', '632822000000', '都兰县', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3557', '632823000000', '天峻县', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3558', '632857000000', '大柴旦行政委员会', '3', '632800000000', '3551', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3559', '640000000000', '宁夏回族自治区', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3560', '640100000000', '银川市', '2', '640000000000', '3559', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3561', '640101000000', '市辖区', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3562', '640104000000', '兴庆区', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3563', '640105000000', '西夏区', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3564', '640106000000', '金凤区', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3565', '640121000000', '永宁县', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3566', '640122000000', '贺兰县', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3567', '640181000000', '灵武市', '3', '640100000000', '3560', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3568', '640200000000', '石嘴山市', '2', '640000000000', '3559', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3569', '640201000000', '市辖区', '3', '640200000000', '3568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3570', '640202000000', '大武口区', '3', '640200000000', '3568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3571', '640205000000', '惠农区', '3', '640200000000', '3568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3572', '640221000000', '平罗县', '3', '640200000000', '3568', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3573', '640300000000', '吴忠市', '2', '640000000000', '3559', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3574', '640301000000', '市辖区', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3575', '640302000000', '利通区', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3576', '640303000000', '红寺堡区', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3577', '640323000000', '盐池县', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3578', '640324000000', '同心县', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3579', '640381000000', '青铜峡市', '3', '640300000000', '3573', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3580', '640400000000', '固原市', '2', '640000000000', '3559', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3581', '640401000000', '市辖区', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3582', '640402000000', '原州区', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3583', '640422000000', '西吉县', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3584', '640423000000', '隆德县', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3585', '640424000000', '泾源县', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3586', '640425000000', '彭阳县', '3', '640400000000', '3580', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3587', '640500000000', '中卫市', '2', '640000000000', '3559', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3588', '640501000000', '市辖区', '3', '640500000000', '3587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3589', '640502000000', '沙坡头区', '3', '640500000000', '3587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3590', '640521000000', '中宁县', '3', '640500000000', '3587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3591', '640522000000', '海原县', '3', '640500000000', '3587', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3592', '650000000000', '新疆维吾尔自治区', '1', '0', '0', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3593', '650100000000', '乌鲁木齐市', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3594', '650101000000', '市辖区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3595', '650102000000', '天山区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3596', '650103000000', '沙依巴克区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3597', '650104000000', '新市区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3598', '650105000000', '水磨沟区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3599', '650106000000', '头屯河区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3600', '650107000000', '达坂城区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3601', '650109000000', '米东区', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3602', '650121000000', '乌鲁木齐县', '3', '650100000000', '3593', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3603', '650200000000', '克拉玛依市', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3604', '650201000000', '市辖区', '3', '650200000000', '3603', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3605', '650202000000', '独山子区', '3', '650200000000', '3603', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3606', '650203000000', '克拉玛依区', '3', '650200000000', '3603', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3607', '650204000000', '白碱滩区', '3', '650200000000', '3603', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3608', '650205000000', '乌尔禾区', '3', '650200000000', '3603', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3609', '650400000000', '吐鲁番市', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3610', '650402000000', '高昌区', '3', '650400000000', '3609', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3611', '650421000000', '鄯善县', '3', '650400000000', '3609', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3612', '650422000000', '托克逊县', '3', '650400000000', '3609', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3613', '650500000000', '哈密市', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3614', '650502000000', '伊州区', '3', '650500000000', '3613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3615', '650521000000', '巴里坤哈萨克自治县', '3', '650500000000', '3613', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3616', '650522000000', '伊吾县', '3', '650500000000', '3613', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3617', '652300000000', '昌吉回族自治州', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3618', '652301000000', '昌吉市', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3619', '652302000000', '阜康市', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3620', '652323000000', '呼图壁县', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3621', '652324000000', '玛纳斯县', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3622', '652325000000', '奇台县', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3623', '652327000000', '吉木萨尔县', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3624', '652328000000', '木垒哈萨克自治县', '3', '652300000000', '3617', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3625', '652700000000', '博尔塔拉蒙古自治州', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3626', '652701000000', '博乐市', '3', '652700000000', '3625', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3627', '652702000000', '阿拉山口市', '3', '652700000000', '3625', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3628', '652722000000', '精河县', '3', '652700000000', '3625', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3629', '652723000000', '温泉县', '3', '652700000000', '3625', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3630', '652800000000', '巴音郭楞蒙古自治州', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3631', '652801000000', '库尔勒市', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3632', '652822000000', '轮台县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3633', '652823000000', '尉犁县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3634', '652824000000', '若羌县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3635', '652825000000', '且末县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3636', '652826000000', '焉耆回族自治县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3637', '652827000000', '和静县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3638', '652828000000', '和硕县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3639', '652829000000', '博湖县', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3640', '652871000000', '库尔勒经济技术开发区', '3', '652800000000', '3630', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3641', '652900000000', '阿克苏地区', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3642', '652901000000', '阿克苏市', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3643', '652902000000', '库车市', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3644', '652922000000', '温宿县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3645', '652924000000', '沙雅县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3646', '652925000000', '新和县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3647', '652926000000', '拜城县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3648', '652927000000', '乌什县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3649', '652928000000', '阿瓦提县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3650', '652929000000', '柯坪县', '3', '652900000000', '3641', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3651', '653000000000', '克孜勒苏柯尔克孜自治州', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3652', '653001000000', '阿图什市', '3', '653000000000', '3651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3653', '653022000000', '阿克陶县', '3', '653000000000', '3651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3654', '653023000000', '阿合奇县', '3', '653000000000', '3651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3655', '653024000000', '乌恰县', '3', '653000000000', '3651', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3656', '653100000000', '喀什地区', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3657', '653101000000', '喀什市', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3658', '653121000000', '疏附县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3659', '653122000000', '疏勒县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3660', '653123000000', '英吉沙县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3661', '653124000000', '泽普县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3662', '653125000000', '莎车县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3663', '653126000000', '叶城县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3664', '653127000000', '麦盖提县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3665', '653128000000', '岳普湖县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3666', '653129000000', '伽师县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3667', '653130000000', '巴楚县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3668', '653131000000', '塔什库尔干塔吉克自治县', '3', '653100000000', '3656', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3669', '653200000000', '和田地区', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3670', '653201000000', '和田市', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3671', '653221000000', '和田县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3672', '653222000000', '墨玉县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3673', '653223000000', '皮山县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3674', '653224000000', '洛浦县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3675', '653225000000', '策勒县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3676', '653226000000', '于田县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3677', '653227000000', '民丰县', '3', '653200000000', '3669', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3678', '654000000000', '伊犁哈萨克自治州', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3679', '654002000000', '伊宁市', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3680', '654003000000', '奎屯市', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3681', '654004000000', '霍尔果斯市', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3682', '654021000000', '伊宁县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3683', '654022000000', '察布查尔锡伯自治县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3684', '654023000000', '霍城县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3685', '654024000000', '巩留县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3686', '654025000000', '新源县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3687', '654026000000', '昭苏县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3688', '654027000000', '特克斯县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3689', '654028000000', '尼勒克县', '3', '654000000000', '3678', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3690', '654200000000', '塔城地区', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3691', '654201000000', '塔城市', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3692', '654202000000', '乌苏市', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3693', '654203000000', '沙湾市', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3694', '654221000000', '额敏县', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3695', '654224000000', '托里县', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3696', '654225000000', '裕民县', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3697', '654226000000', '和布克赛尔蒙古自治县', '3', '654200000000', '3690', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3698', '654300000000', '阿勒泰地区', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3699', '654301000000', '阿勒泰市', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3700', '654321000000', '布尔津县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3701', '654322000000', '富蕴县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3702', '654323000000', '福海县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3703', '654324000000', '哈巴河县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3704', '654325000000', '青河县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3705', '654326000000', '吉木乃县', '3', '654300000000', '3698', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3706', '659000000000', '自治区直辖县级行政区划', '2', '650000000000', '3592', '1', '2022-01-21 13:15:57', null, '0', '0',
        '1');
INSERT INTO `administrative_area`
VALUES ('3707', '659001000000', '石河子市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3708', '659002000000', '阿拉尔市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3709', '659003000000', '图木舒克市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3710', '659004000000', '五家渠市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3711', '659005000000', '北屯市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3712', '659006000000', '铁门关市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3713', '659007000000', '双河市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3714', '659008000000', '可克达拉市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3715', '659009000000', '昆玉市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3716', '659010000000', '胡杨河市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
INSERT INTO `administrative_area`
VALUES ('3717', '659011000000', '新星市', '3', '659000000000', '3706', '1', '2022-01-21 13:15:57', null, '0', '0', '1');
